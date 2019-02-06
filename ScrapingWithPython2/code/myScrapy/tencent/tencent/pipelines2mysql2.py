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


class TencentPipeline(object):
    def process_item(self, item, spider):
        # position_name = scrapy.Field()
        # position_link = scrapy.Field()
        # position_type = scrapy.Field()
        # people_num = scrapy.Field()
        # work_address = scrapy.Field()
        # publish_time = scrapy.Field()

        position_name = item['position_name']
        position_link = item['position_link']
        position_type = item['position_type']
        people_num = item['people_num']
        work_address = item['work_address']
        publish_time = item['publish_time']

        conn = pymysql.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='wsx1001',
                db='dgmissiondb6',
                charset='utf8')
        cur = conn.cursor()
        mysqlCmd = "INSERT INTO tencentpositions" \
                   "(position_name, position_link, position_type, people_num, work_address, publish_time) " \
                   "VALUES('%s', '%s', '%s', '%s', '%s');" \
                   % (position_name, position_link, position_type, people_num, work_address, publish_time)
        cur.execute(mysqlCmd)
        cur.close()
        conn.commit()
        conn.close()

        return item
