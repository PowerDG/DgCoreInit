# -*- coding: utf-8 -*-
import scrapy


class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['mtime.com']
    start_urls = ['http://mtime.com/']

    def parse(self, response):
        pass
