from django.conf import settings
from .models import Listing

User = settings.AUTH_USER_MODEL

# class TCart(object):
#     def __init__(self, request):
#         self.session = request.session
#         tcart = self.session.get(settings.TCART_SESSION_ID)
#
#         if not tcart:
#             tcart = self.session[settings.TCART_SESSION_ID] = {}
#
#         self.tcart = tcart
#
#     def __iter__(self):
#         for p in self.tcart.keys():
#             self.tcart[str(p)]['listing'] = Listing.objects.get(pk=p)
#
#         for list_item in self.tcart.values():
#             list_item['total_price'] = list_item['listing'].price * list_item['quantity']
#
#             yield listing
#
#     def __len__(self):
#         return sum(list_item['quantity'] for list_item in self.tcart.values())
#
#     def add(self, listing_id, quantity=1, update_quantity=False):
#         listing_id = str(listing_id)
#
#         if listing_id not in self.tcart:
#             self.tcart[listing_id] = {'quantity': 1, 'id': listing_id}
#
#         if update_quantity:
#             self.tcart[listing_id]['quantity'] += int(quantity)
#
#             if self.tcart[listing_id]['quantity'] == 0:
#                 self.remove(listing_id)
#
#         self.save()
#
#     def remove(self, listing_id):
#         if listing_id in self.tcart:
#             del self.tcart[listing_id]
#             self.save()
#
#     def save(self):
#         self.session[settings.TCART_SESSION_ID] = self.tcart
#         self.session.modified = True
#
#     def clear(self):
#         del self.session[settings.TCART_SESSION_ID]
#         self.session.modified = True
#
#     def get_total_cost(self):
#         for p in self.tcart.keys():
#             self.tcart[str(p)]['listing'] = Listing.objects.get(pk=p)
#
#         return sum(list_item['quantity'] * list_item['listing'].price for list_item in self.tcart.values())


