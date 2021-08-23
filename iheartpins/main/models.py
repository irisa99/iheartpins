from django.db import models
from django.conf import settings
from django.utils import timezone
from io import BytesIO
from PIL import Image
from django.core.files import File


User = settings.AUTH_USER_MODEL

class Pinventory(models.Model):
    owner = models.OneToOneField(User, related_name='pinventory', on_delete=models.CASCADE)
    is_public_all = models.BooleanField(verbose_name='public', default=True)
    is_public_listed = models.BooleanField(verbose_name='only listed items', default=True)

    class Meta:
        verbose_name_plural = 'pinventories'

    def verbose_name(self):
        return f"{self.owner}'s pinventory"

    def __str__(self):
        return self.verbose_name()


TYPE_CHOICES = (
    (0, 'Pin'),
    (1, 'Pin Set'),
)

class Item(models.Model):
    name = models.CharField(max_length=255, unique=True)
    is_accepted = models.BooleanField(default=False)
    type = models.BooleanField(default=0, blank=True, null=True)
    source = models.CharField(max_length=120, null=True)
    release_date = models.DateField(blank=True, null=True)
    release_notes = models.CharField(max_length=255, blank=True, null=True)
    edition_type = models.CharField(max_length=30, blank=True, null=True)
    edition_size = models.IntegerField(blank=True, null=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_retired = models.BooleanField(verbose_name='retired', blank=True, null=True)
    retired_date = models.DateField(blank=True, null=True)
    has_ap = models.BooleanField(verbose_name='artist proof', blank=True, null=True, default=False)
    ap_qty = models.IntegerField(blank=True, null=True, default=0)
    has_pp = models.BooleanField(verbose_name='pre-production', blank=True, null=True, default=False)
    pp_qty = models.IntegerField(blank=True, null=True, default=0)
    descrip = models.TextField(verbose_name='description', blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True)
    date_item_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    submitted_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    needs_new_pic = models.BooleanField(blank=True, null=True, default=False)


    def __str__(self):
        return self.name


class PinSet(Item):
    qty_in_set = models.IntegerField(verbose_name='quantity of pins in set')

    def __str__(self):
        return self.name


class Pin(Item):
    is_included_in_set = models.BooleanField(verbose_name='part of a set', default=False)
    is_fantasy = models.BooleanField(verbose_name='fantasy', default=False)
    # related_pins =

    def __str__(self):
        return self.name


class PinSetContent(models.Model):
    set = models.ForeignKey(PinSet, on_delete=models.CASCADE)
    pin_in_set = models.ForeignKey(Pin, on_delete=models.CASCADE)



class ItemImage(models.Model):
    image = models.ImageField(upload_to='images', height_field=None, width_field=None, max_length=100, null=True)
    item = models.ForeignKey(Item, related_name='images', on_delete=models.CASCADE)
    is_primary = models.BooleanField(default=True)
    date_image_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)


class PinventoryContent(models.Model):
    pinventory = models.ForeignKey(Pinventory, on_delete=models.CASCADE, related_name='pinventorycontent')
    item = models.ForeignKey(Item, related_name='pinventorycontent', on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, default=0)
    date_item_added = models.DateTimeField(verbose_name='date added', auto_now_add=True)
    date_qty_update = models.DateTimeField(verbose_name='date updated', default=timezone.now)
    date_removed = models.DateTimeField(blank=True, null=True)
    hidden_for_set = models.BooleanField(default=0)
    status = models.IntegerField(default=1)

    def add_to_pinventory(self, pinventory, item, quantity=1, update_quantity=False):
        item_id = str(item_id)

        if listing_id not in self.pinventory:
            self.pinventory[item_id] = {'quantity': 1, 'id': item_id}

        if update_quantity:
            self.pinventory[item_id]['quantity'] += int(quantity)

            if self.pinventory[item_id]['quantity'] == 0:
                self.remove(item_id)

        self.save()






    def delete_from_pinventory(self, item):
        pass

class UserEstimatedValue(models.Model):
    est_value = models.DecimalField(verbose_name='estimated value', max_digits=10, decimal_places=2, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value_date = models.DateTimeField(auto_now_add=True)




