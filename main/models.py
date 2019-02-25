from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    tag1 = models.CharField(max_length=100)
    tag2 = models.CharField(max_length=100)
    tag3 = models.CharField(max_length=100)
    tag4 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    uri = models.TextField(blank=True)
