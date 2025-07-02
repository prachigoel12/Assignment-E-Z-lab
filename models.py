from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_ops = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

class SharedFile(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
