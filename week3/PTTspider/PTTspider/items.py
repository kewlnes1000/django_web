# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PttspiderItem(scrapy.Item):
    # define the fields for your item here like:
    push = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    href = scrapy.Field()
    date = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()