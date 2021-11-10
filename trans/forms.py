from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

CONDITION_TYPES = (
    (0, 'Mint'),
    (1, 'New'),
    (2, 'Good'),
    (3, 'Fair'),
    (4, 'Other'),
)

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField()
    listing_id = forms.IntegerField()


# class AddToTCartForm(forms.Form):
#     quantity = forms.IntegerField()
#     listing = forms.IntegerField()


