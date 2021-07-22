from django.urls import path
from . import views
from django.contrib.auth import get_user_model


User = get_user_model()

app_name = 'trans'

urlpatterns = [
    # path('item-detail/<slug:item_slug>/', views.item_detail, name='item'),
    path('search-available/', views.search_listings, name='search_available'),
    path('orders/', views.seller_orders, name='orders'),
]