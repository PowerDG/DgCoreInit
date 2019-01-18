# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 定义爬虫最终需要哪些项
class TodaymovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass

    movieTitleCn = scrapy.Field()  # 中文名
    movieTitleEn = scrapy.Field()  # 英文名
    director = scrapy.Field()
    runtime = scrapy.Field()
