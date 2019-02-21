from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    tag = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    uri = models.TextField(blank=True)
