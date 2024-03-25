from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.loginUser, name='loginUser'),
    path('', views.homepage, name='homepage'),
    path('register/', views.createUser, name='registerUser'),
    path('logout/', views.logoutUser, name='logoutUser'),

    path('checkout/<str:pk>/', views.checkout, name='checkout'),
    path('checkoutconfirmation/<str:pk>/', views.checkout_confirmation, name='checkout_confirmation'),
    path('confirmation/', views.confirmation, name='confirmation'),
    path('megacart/', views.megacart, name='megacart'),
    path('megaconfirmatory/<str:pk>/', views.megacart_confirmation, name='megacart_confirmation'),
    path('productdetails/<str:pk>',views.productdetails,name='productdetails'),
    path('checkout/<str:pk>/', views.checkout, name='checkout'),
    path('checkoutconfirmation/<str:pk>/', views.checkout_confirmation, name='checkout_confirmation'),
    path('confirmation/<str:pk>', views.confirmation, name='confirmation'),
    path('purchasehistory/<str:pk>/', views.purchasehistory, name='purchasehistory')
]