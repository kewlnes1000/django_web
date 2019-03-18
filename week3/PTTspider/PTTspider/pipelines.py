# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import string
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline


class PttspiderPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url, meta = {'item': item})

    def file_path(self, request, response = None, info = None):
        item = request.meta['item']
        #取得網址最後一個字串做為檔名
        name = request.url.split('/')[-1]

        return "%s/%s"%(item['title'], name)
    
    def item_completed(self, results, item, info):
        print('in item_completed')
        file_paths = results[0][1].get("path")
        print(file_paths)
        print(item)
        if not file_paths:
            raise DropItem("Item contains no files")
        item['file_urls'] = file_paths
        return item

    
