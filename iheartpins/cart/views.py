from django.shortcuts import render, redirect
import json

from trans.models import Listing
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    # if request.user.is_authenticated:
    #     user = request.user
    # else:
    #     # Create empty cart for now for non-logged in user
    #     items = []
    #
    # context = {'items': items}
    #
    remove_from_cart = request.GET.get('remove_from_cart', '')
    change_quantity = request.GET.get('change_quantity', '')
    quantity = request.GET.get('quantity', 0)

    if remove_from_cart:
        cart.remove(remove_from_cart)
        return redirect('cart:cart')

    if change_quantity:
        cart.add(change_quantity, quantity, True)
        return redirect('cart:cart')

    return render(request, 'cart/cart.html')


# def update_cart(request):
#     data = json.loads(request.data)
#     listing_id = data['listing']
#     action = data['action']
#
#     user = request.user
#     listing = Listing.objects.get(id=listing_id)
#
#     return render(request,'cart/cart.html')

