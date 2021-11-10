from django.urls import path
from . import views


urlpatterns = [
    path('', views.account, name='account'),
    path('login/',views.login, name='login'),
    path('logout/' , views.Logout , name="logout"),
    path('register/',views.register, name='register'),
    path('tokenverify/',views.TokenVerify, name='tokenverify'),
    path('verify/<auth_token>',views.verify, name='verify'),
    path('forgotpassword/',views.forgot_password, name='forgotpassword'),
    path('resetpassword/<str:resettoken>',views.reset_password, name='resetpassword'),
]
