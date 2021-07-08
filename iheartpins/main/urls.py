from django.urls import path
from . import views
from django.contrib.auth import get_user_model


User = get_user_model()

app_name = 'main'

urlpatterns = [
    path('home/', views.home, name="home"),
    path('pinventory/', views.pinventory, name='pinventory'),
    path('search/', views.search_pindex, name='search'),
    path('item-detail/<slug:item_slug>/', views.item_detail, name='item'),
    path('submit-item/', views.submit_item, name='submit'),
    path('contact-us/', views.contact_us, name="contact"),
    path('', views.home, name="home"),
]