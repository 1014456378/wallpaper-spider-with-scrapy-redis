# -*- coding: utf-8 -*-
from Wallpaper.items import WallpaperItem
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
import re


class WallpaperSpider(RedisCrawlSpider):
    name = 'wallpaper'
    allowed_domains = ['alpha.wallhaven.cc']
    base_url = 'https://alpha.wallhaven.cc/search?q=girl&page='
    n = 1
    redis_key = 'WallpaperSpider:start_url'

    # start_urls = ['https://alpha.wallhaven.cc/search?q=girl&page=1']

    def parse(self, response):
        for href in response.css('a::attr(href)').extract():
            try:
                d = re.findall(r'https://alpha.wallhaven.cc/wallpaper/\d{6}', href)[0]
                yield scrapy.Request(d, callback=self.parse_stock)
            except:
                continue

        self.n += 1
        yield scrapy.Request(self.base_url + str(self.n), callback=self.parse)

    def parse_stock(self, response):
        for src in response.css('img::attr(src)').extract():
            data1 = re.findall(r'//wallpapers.*\d\.png', src)
            # print(len(data))
            if len(data1) == 0:
                data2 = re.findall(r'//wallpapers.*\d\.jpg', src)
                if len(data2) == 0:
                    print("找不到")
                else:
                    data_list = data2[0]
                    item = WallpaperItem()
                    item['imagelink'] = 'https:' + data_list
                    print(item['imagelink'])
                    yield item

            else:
                data_list = data1[0]
                item = WallpaperItem()
                item['imagelink'] = 'https:' + data_list
                print(item['imagelink'])
                yield item
