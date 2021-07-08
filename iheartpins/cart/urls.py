from django.urls import path
from django.contrib.auth import get_user_model
from . import views

User = get_user_model()

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name="cart"),
]




