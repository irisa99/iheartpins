from django.http import response
from cart.cart import Cart
from .models import Order, OrderItem
from paypalcheckoutsdk.orders import OrdersGetRequest
from.paypal import PayPalClient


def checkout(request, user, email, ship_to, cart_total, shipping, sales_tax, total_paid, gateway):
    cart = Cart(request)
    order = Order.objects.create(
        buyer=user,
        buyer_firstname=user.name.firstname,
        buyer_lastname=user.name.lastname,
        email=user.email,
        ship_to=user.name.address.get(is_shipping=True),
        cart_total=cart_total,
        shipping=shipping,
        sales_tax=sales_tax,
        total_paid=total_paid,
        gateway=gateway,
    )

    for cart_item in Cart(request):
        OrderItem.objects.create(
            order=order,
            listing=cart_item['listing'],
            quantity=cart_item['quantity'],
            price=cart_item['listing'].price,
            seller=cart_item['listing'].pinventory.owner,
        )
    return order

