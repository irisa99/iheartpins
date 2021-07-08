from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset
from crispy_forms.bootstrap import InlineRadios, Div
from .models import ItemImage, Pin, PinSet, Item


User = get_user_model()

TYPE_CHOICES = (
    (0, 'Pin'),
    (1, 'Pin Set'),
)


def get_formhelper_submit():
    helper = FormHelper()
    layout = Layout()
    fieldset = Fieldset('SelectType')


class SelectType(forms.ModelForm):
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect(attrs={'onchange':'submit();'}),initial=0)
    class Meta:
        model = Item
        fields = ['type']


class SubmitPin(forms.ModelForm):
    class Meta:
        model = Pin
        fields = [
            'name',
            'source',
            'release_date',
            'release_notes',
            'edition_type',
            'edition_size',
            'original_price',
            'is_retired',
            'retired_date',
            'has_ap',
            'has_pp',
            'is_included_in_set',
            'is_fantasy',
        ]

class SubmitPinSet(forms.ModelForm):
    class Meta:
        model = PinSet
        fields = [
            'name',
            'source',
            'release_date',
            'release_notes',
            'edition_type',
            'edition_size',
            'original_price',
            'is_retired',
            'retired_date',
            'has_ap',
            'has_pp',
            'qty_in_set',
        ]



class SubmitImage(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        model = ItemImage
        fields = ['image',]
    pass

