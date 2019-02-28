from django.contrib import admin

# Register your models here.
from main.models import Article
from main.models import Lists

admin.site.register(Article)
admin.site.register(Lists)