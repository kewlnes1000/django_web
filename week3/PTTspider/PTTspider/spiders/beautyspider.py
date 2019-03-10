# -*- coding: utf-8 -*-
import scrapy
from scrapy.exceptions import CloseSpider
from ..items import PttspiderItem

class BeautySpider(scrapy.Spider):
    name = 'Beauty'
    count_page = 1
    allowed_domains = ['www.ptt.cc/']
    start_urls = ['https://www.ptt.cc/bbs/Beauty/index.html']
    


    def parse(self, response):
        items = PttspiderItem()
        # for article in response.css('div.r-ent'):
        #     items['push'] = article.css('div.nrec > span.hl::text').extract_first()
        #     items['title'] = article.css('div.title > a::text').extract_first()
        #     items['href'] = article.css('div.title > a::attr("href")').extract()
        #     items['author'] = article.css('div.meta > div.author::text').extract_first()
        #     yield(items)


        for href in response.css('div.r-ent > div.title > a::attr("href")'):
            full_url = response.urljoin(href.extract())
            print(full_url)
            yield scrapy.Request(full_url, callback=self.page_parse, dont_filter = True)


        next_page_url = response.css('div.action-bar > div.btn-group-paging > a.btn::attr("href")')[1].extract()
        if (next_page_url) and (self.count_page < 10):
            self.count_page = self.count_page + 1 
            new = response.urljoin(next_page_url) 
        else:   
            raise  CloseSpider('close it')
        yield scrapy.Request(new, callback = self.parse, dont_filter = True)

    def page_parse(self, response):
        items = PttspiderItem()
        items['date'] = response.css('div.article-metaline > span.article-meta-value').extract()
        for img in response.css('div.embed-main-image > div#image > img::attr("src")'):
            if img.extract().find('http') == -1 :
                imageURL = "http:" + img.extract()
            else :
                imageURL = img.extract()
            print(imageURL)
            yield PttspiderItem(file_urls=[imageURL])
