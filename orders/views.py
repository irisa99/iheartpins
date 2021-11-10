from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.conf import settings
from django.http import request, HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json
import ast

from decimal import Decimal

from paypalcheckoutsdk.orders import OrdersGetRequest
from .paypal import PayPalClient

from cart.cart import Cart
from trans.models import Listing
from main.models import PinventoryContent
from .utilities import checkout
from django.contrib.auth import get_user_model
from .shippingRate import getShippingRate
from .taxRate import get_tax
from accounts.models import Address, Person

User = get_user_model()

@login_required
def payment(request):
    cart = Cart(request)
    user = request.user
    email = user.email
    ship_to = request.user.name.address.get(is_shipping=True)
    cart_total = float(cart.get_total_price())
    shipping = 0.00
    sales_tax = 0.00
    seller_items = []
    sellers = []
    # seller_addresses = []
    for cart_item in Cart(request):
        item_seller = cart_item['seller']
        item_price = cart_item['listing']['price']
        seller_items.append((item_seller, item_price))
        if item_seller not in sellers:
            sellers.append(item_seller)

    for seller in sellers:
        slr = json.loads(seller)
        person = Person.objects.get(pk=slr['id'])
        seller_address = person.address.filter(is_shipping=True)
        seller_total = [item_price for item_seller, item_price in seller_items if seller == item_seller]
        # sales_tax_by_seller = get_tax(senderAddress=seller_address, receiverAddress=ship_to, orderAmount=seller_total, shippingAmount=shipping)

    total_paid = cart_total + shipping + sales_tax

    if request.method == 'POST':

        data = json.loads(request.body)
        gateway = data['gateway']
        payment_intent = data['order_id']

        order = checkout(request, user, cart_total, shipping, sales_tax, total_paid, gateway, payment_intent)
        order.save()

        if gateway == 'paypal':
            PPClient = PayPalClient()
            req = OrdersGetRequest(payment_intent)
            response = PPClient.client.execute(req)

            if response.result.status == 'COMPLETED':
                order.paid = True
                order.status = 'paid'
                order.save()
                cart.clear()

                jsonresponse = {'success': True}
                return JsonResponse(jsonresponse)

            else:
                jsonresponse = {'success': False}
                return JsonResponse(jsonresponse)

        else:
            jsonresponse = {'success': False}
            return JsonResponse(jsonresponse)
    else:
        context = {
            'cart': cart,
            'user': user,
            'ship_to': ship_to,
            'shipping': shipping,
            'sales_tax': sales_tax,
            'total_paid': total_paid,
            'paypal_pub_key': settings.PAYPAL_PUB_KEY,
        }
        return render(request, 'orders/checkout.html', context)



def success(request):
    return render(request, 'orders/success.html', {})



