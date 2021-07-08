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
    image = models.ImageField(upload_to='None', height_field=None, width_field=None, max_length=100, null=True)
    listing = models.ForeignKey(Listing, related_name='image', on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=True)
    date_image_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)



