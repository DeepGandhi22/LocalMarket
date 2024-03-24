from django.urls import path
from . import views

urlpatterns = [
    path('createproduct/<str:pk>', views.createProduct, name='createproduct'),
    path('editproduct/<str:pk>', views.editProduct, name='editproduct'),
    path('deleteproduct/<str:pk>', views.deleteProduct, name='deleteproduct'),

]