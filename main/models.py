from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    tag1 = models.CharField(max_length=100,blank=True)
    tag2 = models.CharField(max_length=100,blank=True)
    tag3 = models.CharField(max_length=100,blank=True)
    tag4 = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uri = models.TextField(blank=True)

class Lists(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
