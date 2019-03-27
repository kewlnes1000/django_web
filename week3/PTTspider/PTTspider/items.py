# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from week3.models import PTTspider


class PttspiderItem(DjangoItem):
    # define the fields for your item here like:
    django_model = PTTspider
    files = scrapy.Field()
