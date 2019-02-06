# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    def __init__(self):
        print("=======start========")
        self.file = open("tencent.json", "w", encoding="utf-8")

    def process_item(self, item, spider):
        print("=====ing=======")
        dict_item = dict(item)  # 转换成字典
        json_text = json.dumps(dict_item, ensure_ascii=False) + "\n"
        self.file.write(json_text)
        return item

        def close_spider(self, spider):
            print("=======end===========")

        self.file.close()


# ---------------------
# 作者：a289237642
# 来源：CSDN
# 原文：https: // blog.csdn.net / a289237642 / article / details / 80988583
# 版权声明：本文为博主原创文章，转载请附上博文链接！