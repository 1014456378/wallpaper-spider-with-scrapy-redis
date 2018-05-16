# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import scrapy


class WallpaperPipeline(ImagesPipeline):


    def get_media_requests(self, item, info):

        image_link = item['imagelink']
        yield scrapy.Request(image_link)
# import scrapy
#
# class WallpaperPipeline(object):
#     def process_item(self, item, spider):
#         image_link = item['imagelink']
#         print(image_link)
#         return item



