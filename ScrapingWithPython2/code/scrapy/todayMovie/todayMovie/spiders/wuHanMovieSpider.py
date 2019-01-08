# -*- coding: utf-8 -*-
import scrapy
from todayMovie.items import TodaymovieItem
import re

class WuhanmoviespiderSpider(scrapy.Spider):
    name = 'wuHanMovieSpider'
    allowed_domains = ['mtime.com']
    start_urls = ['http://theater.mtime.com/China_Hubei_Province_Wuhan_Wuchang/4316/']

    def parse(self, response):
        selector = response.xpath('/html/body/script[3]/text()')[0].extract()
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
        return items

