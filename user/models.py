from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    first_name = models.CharField(max_length=21)
    last_name = models.CharField(max_length=21)
    b_date = models.DateField()
    phone = models.CharField(max_length=12)
    email = models.CharField(max_length=51)
    gender = models.CharField(max_length=7)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()

    class Meta:
        db_table = "\"USER\""
