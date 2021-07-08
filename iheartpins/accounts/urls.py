from django.urls import path
from django.contrib.auth import get_user_model
from . import views

User = get_user_model()

urlpatterns = [
    path('profile/', views.user_profile, name='profile'),
]
