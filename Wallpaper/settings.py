# -*- coding: utf-8 -*-

# Scrapy settings for Wallpaper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Wallpaper'

SPIDER_MODULES = ['Wallpaper.spiders']
NEWSPIDER_MODULE = 'Wallpaper.spiders'

#使用了scrapy_redis里的去重软件，不使用scrapy默认的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#使用了scrapy_redis里的调度器组件，不使用scrapy默认的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#使用队列形式
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#允许暂停，redis请求记录不丢失
SCHEDULER_PERSIST = True

IMAGES_STORE = "/home/python/Desktop/Wallpaper/picture"

ROBOTSTXT_OBEY = False



COOKIES_ENABLED = False
HTTPERROR_ALLOWED_CODES = [500]

ITEM_PIPELINES = {
    'Wallpaper.pipelines.WallpaperPipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
REDIS_HOST = '192.168.233.128'
REDIS_PORT = 6379

