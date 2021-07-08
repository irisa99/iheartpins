from django.urls import path
from django.contrib.auth import get_user_model
from . import views

User = get_user_model()

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.order_payment, name="checkout"),
    path('payment/', views.payment, name="payment"),
    path('success/', views.success, name='success'),
]


