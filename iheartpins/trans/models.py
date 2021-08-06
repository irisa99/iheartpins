from django.db import models
from django.http import HttpResponse
from django.conf import settings
from main.models import Item, Pinventory, PinventoryContent

User = settings.AUTH_USER_MODEL

class Listing(models.Model):
    pinventory_content = models.OneToOneField(PinventoryContent, related_name='listing', on_delete=models.CASCADE)
    for_sale = models.BooleanField()
    for_trade = models.BooleanField()
    qty_available = models.IntegerField(verbose_name='quantity available', default=1, null=False)
    condition = models.CharField(max_length=30)
    descrip = models.TextField(verbose_name='description', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    date_listing_created = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    is_inactive = models.BooleanField(default=False)

    # class Meta:
    #     # ordering = ['pinventory_content.date_item_added']
    #     pass
    #
    # def __init__(self, id):
    #     self.id = id=

class ListingImage(models.Model):
    image = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100, null=True)
    listing = models.ForeignKey(Listing, related_name='image', on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=True)
    date_image_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)


class TradeOffer(models.Model):
    sender = models.ForeignKey(User, related_name='sent_offers', on_delete=models.DO_NOTHING)
    receiver = models.ForeignKey(User, related_name='received_offers', on_delete=models.DO_NOTHING)
    offer_item_receive = models.ForeignKey(Listing, related_name='item_offered_receiver', on_delete=models.DO_NOTHING)
    offer_item_send1 = models.ForeignKey(Listing, related_name='item_offered_sender1', blank=True, null=True, on_delete=models.DO_NOTHING)
    offer_item_send2 = models.ForeignKey(Listing, related_name='item_offered_sender2', blank=True, null=True, on_delete=models.DO_NOTHING)
    offer_item_send3 = models.ForeignKey(Listing, related_name='item_offered_sender3', blank=True, null=True, on_delete=models.DO_NOTHING)
    date_offer_sent = models.DateTimeField(auto_now_add=True)
    date_offer_received = models.DateTimeField(blank=True, null=True)
    date_offer_replied = models.DateTimeField(blank=True, null=True)
    is_received = models.BooleanField(default=False)
    is_accepted = models.BooleanField(blank=True, null=True, default=False)
    is_counteroffer = models.BooleanField(blank=True, null=True, default=False)



