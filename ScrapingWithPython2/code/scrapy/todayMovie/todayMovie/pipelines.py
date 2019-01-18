# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import time


# 作用为扫尾的pipelines
# Scrapy爬取网页后  取决于此设置如何处理
class TodaymoviePipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y-%m-%d', time.localtime())
        fileName = '武汉汉街万达广场店' + today + '.txt'
        with codecs.open(fileName, 'a+', 'utf-8') as fp:
            fp.write('%s  %s  %s  %s \r\n' 
                    %(item['movieTitleCn'],
                        item['movieTitleEn'],
                        item['director'],
                        item['runtime']))
        #return item
