# -*- coding: utf-8 -*-
import scrapy


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/']

    def parse(self, response):
        pass
