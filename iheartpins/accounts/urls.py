from django.urls import path,include
from django.contrib.auth import get_user_model
from . import views

User = get_user_model()

urlpatterns = [
    
    path('', views.account_home, name='accounthome'),
    path('login/',views.login, name='login'),
    path('register/',views.register, name='register'),
    path('tokenverify/',views.TokenVerify, name='tokenverify'),
    path('verify/<auth_token>',views.verify, name='verify'),
    
]
