from django.db import models

# Create your models here.

# Creating model of CustomUser where we will fetch user details from saleforce api

class CustomUser(models.Model):
    access_token = models.CharField(max_length=1000)
    signature = models.CharField(max_length=1000)
    instance_url = models.CharField(max_length=1000)
    user_id = models.CharField(max_length=1000, unique=True)
    token_type = models.CharField(max_length=30)
    issued_at = models.CharField(max_length=500)
    
    def __str__(self):
        return self.user_id
    