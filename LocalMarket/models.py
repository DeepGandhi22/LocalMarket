import uuid
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from vendor.models import shop

# Create your models here.
class Product(models.Model):
    product_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=200)
    category_name = models.CharField(max_length=200)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])
    amount = models.FloatField(validators=[MinValueValidator(0)])
    description = models.TextField()

    def __str__(self):
        return self.product_name

class Customer(User):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    address = models.CharField(max_length=200, null=False, blank=False)
    phone_regex = (RegexValidator
                   (regex=r'^\d{10}$',
                    message="The phone number should be of 10 digits long"))

    phone_number = models.CharField(validators=[phone_regex], max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Order(models.Model):
    order_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop_id = models.ForeignKey(shop, on_delete=models.CASCADE)
    order_status_choices = [('0', 'Cancelled'), ('1', 'Placed'), ('2', 'Shipped'), ('3', 'Delivered')]
    order_status = models.CharField(max_length=1, choices=order_status_choices, default='1')
    total_amount = models.FloatField()
    user_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.first_name + " " + self.order_id