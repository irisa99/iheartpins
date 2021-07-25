from django.db import models
from django.conf import settings
from trans.models import Listing
from accounts.models import Address, Person


User = settings.AUTH_USER_MODEL

class Order(models.Model):
    buyer = models.ForeignKey(User, related_name='orders', on_delete=models.DO_NOTHING)
    buyer_firstname = models.CharField(max_length=255)
    buyer_lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True)
    ship_to = models.ForeignKey(Address, related_name='orders', on_delete=models.DO_NOTHING)

    status = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    cart_total = models.DecimalField(max_digits=10, decimal_places=2)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    sales_tax = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)

    # order_key = models.CharField(max_length=255)
    gateway = models.CharField(max_length=255, blank=True, null=True)
    payment_intent = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return '%s' % self.id

    def get_total_quantity(self):
        return sum(int(item.quantity) for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, related_name='order_item', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    seller_payout = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payout_complete = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % self.listing

    def get_total_price(self):
        return self.price * self.quantity


