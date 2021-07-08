from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse, HttpResponse


from .forms import AddToCartForm
from cart.cart import Cart
from .models import Listing, ListingImage
from main.models import Item, PinventoryContent, Pinventory
from main.serializers import ListingSerializer


def search_listings(request):
    query = request.GET.get('query', '')
    qitem = Item.objects.filter(Q(id__icontains=query))
    v_content = PinventoryContent.objects.filter(item__in=qitem)
    listings = Listing.objects.filter(pinventory_content__in=v_content, is_inactive=False)
    s_listings = ListingSerializer(listings, many=True, read_only=True).data
    cart = Cart(request)
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            listing_id = form.cleaned_data['listing_id']
            quantity = form.cleaned_data['quantity']
            cart.add(listing_id=listing_id, quantity=quantity, update_quantity=False)
            messages.success(request, 'Item added to cart successfully.')
            return redirect('trans:search_available')
    else:
        form = AddToCartForm()
    return render(request,'trans/search_available.html', {
        'form': form,
        'query': query,
        'qitem': qitem,
        'v_content': v_content,
        'listings': s_listings,
    })




def trade_offers_detail(request):
    return render(request, 'trans/trade_offers.html')



