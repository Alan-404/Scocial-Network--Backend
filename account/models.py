from django.db import models
from user.models import User

# Create your models here.

class Account(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    user_id = models.CharField(max_length=21)
    password = models.CharField(max_length=101)
    role = models.CharField(max_length=11)
    status = models.BooleanField(default=True)
    modified_at = models.DateTimeField()
    class Meta:
        db_table = "account"
