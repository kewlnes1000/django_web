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
        print('in get_media_requests')
        print(item)
        for file_url in item['file_urls']:
            yield scrapy.Request(file_url, meta = {'item': item})
    
    def item_completed(self, results, item, info):
        print('in item_completed')
        print(item)
        print(results)
        file_paths = [x['path'] for ok, x in results if ok]
        if not file_paths:
            raise DropItem("Item contains no files")
        # item['file_paths'] = file_paths
        return item

    def file_path(self, request, response = None, info = None):
        print('in file_path')
        print(request.url)
        item = request.meta['item']
        print(item)

        #取得網址最後一個字串做為檔名
        name = request.url.split('/')[-1]
        print(name)
        filename = u'full/{0}/{1}'.format(item['title'], name)
        print(filename)

        return filename
