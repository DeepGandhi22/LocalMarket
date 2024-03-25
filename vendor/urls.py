from django.urls import path
from . import views

urlpatterns = [

    path('login/', views.loginVendor, name='loginVendor'),
    path('register/', views.createVendor, name='registerVendor'),
    path('logout/', views.logoutVendor, name='logoutVendor'),

    path('createproduct/<str:pk>', views.createProduct, name='createproduct'),
    path('editproduct/<str:pk>', views.editProduct, name='editproduct'),
    path('deleteproduct/<str:pk>', views.deleteProduct, name='deleteproduct'),

    path('shopview/<str:pk>/', views.shopview, name='shopview'),
    path('productdetails/<str:pk>', views.productdetails, name='productdetails')
]