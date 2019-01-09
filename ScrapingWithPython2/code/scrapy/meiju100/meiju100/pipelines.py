# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
import codecs

class Meiju100Pipeline(object):
    def process_item(self, item, spider):
        today = time.strftime('%Y%m%d', time.localtime())
        fileName = today + 'meiju.txt'
        with codecs.open(fileName, 'a', 'utf-8') as fp:
            fp.write("%s \t" %(item['storyName']))
            fp.write("%s \t" %(item['storyState']))
            if len(item['tvStation']) == 0:
                fp.write("unknow \t")
            else:
                fp.write("%s \t" %(item['tvStation'][0]))
            fp.write("%s \n" %(item['updateTime']))
        return item



        return item
