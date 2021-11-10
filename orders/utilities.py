from django.http import response
from cart.cart import Cart
from .models import Order, OrderItem
from trans.models import Listing
from main.models import Pinventory, PinventoryContent
from django.contrib.auth import get_user_model

User = get_user_model()



def checkout(request, user, cart_total, shipping, sales_tax, total_paid, gateway, payment_intent):
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
        payment_intent=payment_intent,
    )

    for cart_item in Cart(request):
        listing = Listing.objects.get(pk=cart_item['listing']['id'])
        v = PinventoryContent.objects.get(pk=cart_item['listing']['pinventory_content']['id'])
        seller = User.objects.get(pk=v.pinventory.owner.id)
        OrderItem.objects.create(
            order=order,
            listing=listing,
            quantity=cart_item['quantity'],
            price=cart_item['listing']['price'],
            seller=seller,
        )
    return order

