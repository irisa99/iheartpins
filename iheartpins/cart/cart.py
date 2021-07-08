from django.conf import settings
from trans.models import Listing
import simplejson as json
from main.serializers import ListingSerializer

User = settings.AUTH_USER_MODEL

class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        for i in self.cart.keys():
            listings = Listing.objects.filter(pk=i)
            s_listings = ListingSerializer(listings, many=True)
            for s_listing in s_listings.data:
                self.cart[str(i)]['listing'] = s_listing

        for cart_item in self.cart.values():
            cart_item['total_price'] = float(cart_item['listing']['price']) * cart_item['quantity']
            cart_item['total'] = json.dumps(cart_item['total_price'])

            yield cart_item


    def __len__(self):
        return sum(cart_item['quantity'] for cart_item in self.cart.values())

    def add(self, listing_id, quantity, update_quantity=False):
        listing_id = str(listing_id)

        if listing_id not in self.cart:
            self.cart[listing_id] = {'quantity': quantity, 'id': listing_id}

        if update_quantity:
            self.cart[listing_id]['quantity'] += int(quantity)

            if self.cart[listing_id]['quantity'] == 0:
                self.remove(listing_id)

        self.save()

    def remove(self, listing_id):
        if listing_id in self.cart:
            del self.cart[listing_id]
            self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

    def get_total_price(self):
        for i in self.cart.keys():
            self.cart[str(i)]['listing'] = Listing.objects.get(pk=i)

            return sum([cart_item['total_price'] for cart_item in self.cart.values()])




            # return [cart_item for cart_item in self.cart.values()]


            # listings = Listing.objects.filter(pk=i)
            # s_listings = ListingSerializer(listings, many=True)
            # for s_listing in s_listings.data:
            #     self.cart[str(i)]['listing'] = s_listing
            #     return s_listing['price']

                # return cart_item['total_price']


            # return sum(cart_item[i]['quantity'] * float(cart_item[i]['listing']['price']))

