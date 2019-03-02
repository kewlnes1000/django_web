from django.db import models

# Create your models here.

class Messages(models.Model):
    subject = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    to = models.EmailField(max_length=254)
    sent = models.BooleanField(default=False)