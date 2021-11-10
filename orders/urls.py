from django.urls import path
from django.contrib.auth import get_user_model
from . import views

User = get_user_model()

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.payment, name='checkout'),
    path('success/', views.success, name='success'),
]


