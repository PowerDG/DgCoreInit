# -*- coding: utf-8 -*-
#! /usr/bin/python

import scrapy


# from todayMovie.items import TodaymovieItem
from ScrapingWithPython2.code.scrapy.todayMovie.todayMovie.items import TodaymovieItem
# from .todayMovie.items import TodaymovieItem


import re
import sys
import os

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

# scrapy hemspider命令创建的爬虫文件
class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'  # 爬虫名
    allowed_domains = ['mtime.com']  # 定义的域范围
    start_urls = ['http://theater.mtime.com/China_Hubei_Province_Wuhan_Wuchang/4316/']
# 武汉。。影院主页
    def parse(self, response):
        # response 请求返回的数据额
        # 第四个body下的script标签
        selector = response.xpath('/html/body/script[3]/text()')[0].extract()
        print(selector)
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

