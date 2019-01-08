# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs

class GetproxyPipeline(object):
    def process_item(self, item, spider):
        fileName = 'proxy.txt'
        with codecs.open(fileName, 'a', 'utf-8') as fp:
            fp.write("{'%s': '%s://%s:%s'}||\t %s \t %s \t %s \r\n" 
            %(item['protocol'].strip(), item['protocol'].strip(), item['ip'].strip(), item['port'].strip(), item['type'].strip(), item['loction'].strip(), item['source'].strip()))
        return item
