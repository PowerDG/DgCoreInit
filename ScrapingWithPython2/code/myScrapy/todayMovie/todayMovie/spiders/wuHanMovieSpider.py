# -*- coding: utf-8 -*-
import scrapy
import re
import sys
import os

from todayMovie.items import TodaymovieItem


class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['mtime.com']
    # start_urls = ['http://mtime.com/']

    # def parse(self, response):
    #     pass
    start_urls = ['http://theater.mtime.com/China_Hubei_Province_Wuhan_Wuchang/4316/']

    # 武汉。。影院主页
    def parse(self, response):
        # response 请求返回的数据额
        # 第四个body下的script标签
        selector = response.xpath('/html/body/script[3]/text()')[0].extract()
        # print(selector)
        moviesStr = re.search('"movies":\[.*?\]', selector).group()
        moviesList = re.findall('{.*?}', moviesStr)
        items = []
        for movie in moviesList:
            mDic = eval(movie)
            item = TodaymovieItem()
            item['movieTitleCn'] = mDic.get('movieTitleCn')
            item['movieTitleEn'] = mDic.get('movieTitleEn')
            item['director'] = mDic.get('director')
            item['runtime'] = mDic.get('runtime')
            items.append(item)
        # print(items.count())
        return items


