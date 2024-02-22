import uuid
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

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