from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('profile_orders', views.profile_orders, name='profile_orders'),
    path('order_history/<order_number', views.order_history, name='order_history'),
]