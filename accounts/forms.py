from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Person


User = get_user_model()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# class UserPersonRegForm():
#
#     class Meta:
#         model = Person
#         fields = [
#             'firstname',
#             'lastname',
#             'address_street1',
#             'address_street2',
#             'address_city',
#             'address_st',
#             'address_zip',
#             'phone',
#             'gender',
#             'dob',
#         ]
