from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings
from django.http import request, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
import json

from decimal import Decimal

from paypalcheckoutsdk.orders import OrdersCaptureRequest
from paypal.standard.forms import PayPalPaymentsForm
from .paypal import PayPalClient

from cart.cart import Cart
from .forms import CheckoutForm
from .models import Order, OrderItem
from .utilities import checkout
from django.contrib.auth import get_user_model

User = get_user_model()


def payment(request):
    cart = Cart(request)
    user = request.user
    email = user.email
    ship_to = request.user.name.address.get(is_shipping=True)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            cart_total = form.cleaned_data['cart_total']
            shipping = form.cleaned_data['shipping']
            sales_tax = form.cleaned_data['sales_tax']
            total_paid = form.cleaned_data['total_paid']
            print('form is valid')

            data = json.loads(request.body)
            gateway = data['gateway']
            payment_intent = data['order_id']

            order = checkout(request, user, email, ship_to, cart_total, shipping, sales_tax, total_paid, gateway)
            order.save()
            print('order saved')

            if gateway == 'paypal':
                PPClient = PayPalClient()
                req = OrdersCaptureRequest(payment_intent)
                response = PPClient.execute(req)

                if response.result.status == 'COMPLETED':
                    order.paid = True
                    order.payment_intent = payment_intent
                    order.save()

                    jsonresponse = {'success': True}
                    return JsonResponse(jsonresponse)

                else:
                    jsonresponse = {'success': False}
                    return JsonResponse(jsonresponse)

            else:
                jsonresponse = {'success': False}
                return JsonResponse(jsonresponse)
        else:
            jsonresponse = {'success': False}
            return JsonResponse(jsonresponse)

    else:
        form = CheckoutForm()

        context = {
            'cart': cart,
            'user': user,
            'form': form,
            'ship_to': ship_to,
            'paypal_pub_key': settings.PAYPAL_PUB_KEY,
        }
        return render(request, 'orders/checkout.html', context)


def order_payment(request):
    cart = Cart(request)
    user = User.objects.get(pk=2)
    email = user.email
    ship_to = request.user.name.address.get(is_shipping=True)

    payment_intent = ''

    if request.method == 'POST':
        form = CheckoutForm(request.POST)

        if form.is_valid():
            data = json.loads(request.body)
            gateway = data['gateway']

            cart_total = data['cart_total']
            shipping = data['shipping']
            sales_tax = data['sales_tax']
            total_paid = data['total_paid']

            order = checkout(request, user, email, ship_to, cart_total, shipping, sales_tax, total_paid)
            orderid = order.id

            # if order.gateway == 'paypal':
            #     paypal_order_id = data['order_id']
            #     PPClient = PayPalClient()
            #
            #     request = OrdersCaptureRequest(order_id)
            #     response = PPClient.execute(request)
            #
            #     order = Order.objects.get(pk=orderid)
            #
            #     if response.result.status == 'COMPLETED':
            #         order.paid = True
            #         order.payment_intent = orderid
            #         order.save()

                    # cart.clear()

                    # notify_customer(order)
                    # notify_vendor(order)

            #         return redirect('orders:success')
            #     else:
            #         return redirect('main:home')
            # else:
            #     return redirect('main:home')


        else:
            return render(request, 'orders/success.html')

    else:
        form = CheckoutForm()

        context = {
            'cart': cart,
            'user': user,
            'form': form,
            'ship_to': ship_to,
            'paypal_pub_key': settings.PAYPAL_PUB_KEY,
        }
        return render(request, 'orders/checkout.html', context)



def success(request):
    return render(request, 'orders/success.html', {})



