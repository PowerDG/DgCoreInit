# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    people_num = scrapy.Field()
    work_address = scrapy.Field()
    publish_time = scrapy.Field()

#
# ---------------------
# 作者：a289237642
# 来源：CSDN
# 原文：https: // blog.csdn.net / a289237642 / article / details / 80988583
# 版权声明：本文为博主原创文章，转载请附上博文链接！
