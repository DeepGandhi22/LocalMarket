import uuid
from django.db import models
from django.contrib.auth.models import User
from LocalMarket.models import Product
from django.core.validators import RegexValidator

# Create your models here.
class vendor(User):
    vendor_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    phone_regex = (RegexValidator
                   (regex=r'^\d{10}$',
                    message="The phone number should be of 10 digits long"))

    phone_number = models.CharField(validators=[phone_regex], max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class shop(models.Model):
    shop_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    shop_name = models.CharField(max_length=200)
    shop_address = models.TextField(max_length=500)
    vendor_id = models.ForeignKey(vendor, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.shop_name}"