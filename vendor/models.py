import uuid
from django.db import models
from django.contrib.auth.models import User
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