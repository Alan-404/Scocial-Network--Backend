from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.CharField(max_length=21, primary_key=True)
    user_id = models.CharField(max_length=21)
    content = models.TextField()
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    class Meta:
        db_table = 'post'