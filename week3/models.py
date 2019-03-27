from django.db import models

# Create your models here.

class PTTspider(models.Model):
    href = models.CharField(max_length=255)
    push = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    file_urls = models.CharField(max_length=255)

    def __str__(self):
        return self.title