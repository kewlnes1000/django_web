# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from ..items import PttspiderItem

def isImageFormat(link):
    if(link.find('.jpg') > -1 or link.find('.png') > -1 or link.find('.gif') > -1 or link.find('.jpeg') > -1):
       return True
    return False

class BeautySpider(scrapy.Spider):
    name = 'Beauty'
    count_page = 1
    # allowed_domains = ['www.ptt.cc/']
    start_urls = ['https://www.ptt.cc/bbs/Beauty/index.html']
    


    def parse(self, response):
        for article in response.css('div.r-ent'):
            item = PttspiderItem()
            item['href'] = article.css('div.title > a::attr("href")').extract_first()
            item['push'] = article.css('div.nrec > span.hl::text').extract_first()
            item['title'] = article.css('div.title > a::text').extract_first()
            item['author'] = article.css('div.meta > div.author::text').extract_first()
            for url in article.css('div.title a::attr(href)').extract():
                url = response.urljoin(url)
                yield scrapy.Request(url, callback = self.parse_images, meta={'item': item}) 


        next_page_url = response.css('div.action-bar > div.btn-group-paging > a.btn::attr("href")')[1].extract()
        if (next_page_url) and (self.count_page < 1):
            self.count_page = self.count_page + 1 
            new = response.urljoin(next_page_url) 
            yield scrapy.Request(new, callback = self.parse, dont_filter = True)

    def parse_images(self, response):
        item = response.meta['item']
        imgurls = []
        item['date'] = response.css('div.article-metaline > span.article-meta-value::text')[2].extract()
        for img in response.css('a::attr("href")'):
            url = img.extract()
            if(isImageFormat(url)):
               imgurls.append(url)
        item['file_urls'] = imgurls
        return  item
