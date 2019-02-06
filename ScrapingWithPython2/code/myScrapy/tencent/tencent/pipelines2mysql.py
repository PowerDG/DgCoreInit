# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
# pip3 install PyMySQL
# Python3 MySQL 数据库连接 - PyMySQL 驱动
# http://www.runoob.com/python3/python3-mysql.html

# mysql -u root -p
# SHOW VAERIABLES LIKE "character%";


class WeatherPipeline(object):
    def process_item(self, item, spider):
        cityDate = item['cityDate']
        week = item['week']
        temperature = item['temperature']
        weather = item['weather']
        wind = item['wind']

        conn = pymysql.connect(
                host = 'localhost',
                port = 3306,
                user = 'crawlUSER',
                passwd = 'crawl123',
                db = 'scrapyDB',
                charset = 'utf8')
        cur = conn.cursor()
        mysqlCmd = "INSERT INTO weather(cityDate, week, temperature, weather, wind) VALUES('%s', '%s', '%s', '%s', '%s');" %(cityDate, week, temperature, weather, wind)
        cur.execute(mysqlCmd)
        cur.close()
        conn.commit()
        conn.close()

        return item
