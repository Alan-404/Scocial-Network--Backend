from django.db import models

# Create your models here.

class Account(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    user_id = models.CharField(max_length=21)
    password = models.CharField(max_length=101)
    modified_at = models.DateTimeField()
    class Meta:
        db_table = 'account'
