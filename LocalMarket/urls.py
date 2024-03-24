from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('checkout/<str:pk>/', views.checkout, name='checkout'),
    path('checkoutconfirmation/<str:pk>/', views.checkout_confirmation, name='checkout_confirmation'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('megacart/', views.megacart, name='megacart'),
    path('megaconfirmatory/<str:pk>/', views.megacart_confirmation, name='megacart_confirmation')

]