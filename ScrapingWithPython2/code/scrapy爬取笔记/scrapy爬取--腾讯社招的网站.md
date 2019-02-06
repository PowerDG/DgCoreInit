# scrapy爬取--腾讯社招的网站

​	 																				2018年07月10日 16:55:16		[a289237642](https://me.csdn.net/a289237642)	阅读数：217 										

 									

**需求：得到相应的职位、职位类型、职位的链接 、招聘人数、工作地点、发布时间**

**一、**创建Scrapy项目的流程

【本机使用Ancona命令环境】

1）使用命令创建爬虫[腾讯](https://www.baidu.com/s?wd=%E8%85%BE%E8%AE%AF&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)招聘的职位项目：scrapy startproject tencent

2）进程项目命令：cd tencent,并且创建爬虫：scrapy genspider tencentPosition hr.tencent.com

3) 使用[PyCharm](https://www.baidu.com/s?wd=PyCharm&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)打开项目

4）根据需求分析，完成items.py文件的字段

5）完成爬虫的编写

6）管道文件的编程

7）settings.py文件的配置信息

【

 E:\DgProject\PyProject\ScrapingWithPython2\code\myScrapy\tencent

```powershell
(base) E:\DgProject\PyProject\ScrapingWithPython2\code\myScrapy>scrapy startproject tencent
New Scrapy project 'tencent', using template directory 'e:\\programdata\\anaconda3\\lib\\site-packages\\scrapy\\templates\\project', created in:
    E:\DgProject\PyProject\ScrapingWithPython2\code\myScrapy\tencent

You can start your first spider with:
    cd tencent
    scrapy genspider example example.com

(base) E:\DgProject\PyProject\ScrapingWithPython2\code\myScrapy>cd tencent

(base) E:\DgProject\PyProject\ScrapingWithPython2\code\myScrapy\tencent>scrapy genspider tencentPosition hr.tencent.com
Created spider 'tencentPosition' using template 'basic' in module:
  tencent.spiders.tencentPosition
```

】

![img](https://oscimg.oschina.net/oscnet/d1e8ecac9af297c0b5c1ee19dc33009e685.jpg)

8）pycharm打开文件的效果图：

![img](https://oscimg.oschina.net/oscnet/3c43301fc4a8594665f7b4348b64b883d08.jpg)

二、编写各个文件的代码：

1.tencentPosition.py文件

```
import scrapy

from tencent.items import TencentItem


class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['hr.tencent.com']
    offset = 0
    url = "https://hr.tencent.com/position.php?&start="
    start_urls = [url + str(offset) + '#a', ]

    def parse(self, response):
        position_lists = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for postion in position_lists:
            item = TencentItem()
            position_name = postion.xpath("./td[1]/a/text()").extract()[0]
            position_link = postion.xpath("./td[1]/a/@href").extract()[0]
            position_type = postion.xpath("./td[2]/text()").get()
            people_num = postion.xpath("./td[3]/text()").extract()[0]
            work_address = postion.xpath("./td[4]/text()").extract()[0]
            publish_time = postion.xpath("./td[5]/text()").extract()[0]

            item["position_name"] = position_name
            item["position_link"] = position_link
            item["position_type"] = position_type
            item["people_num"] = people_num
            item["work_address"] = work_address
            item["publish_time"] = publish_time
            yield item

            # 下一页的数据
            total_page = response.xpath('//div[@class="left"]/span/text()').extract()[0]
            print(total_page)

            if self.offset < int(total_page):
                self.offset += 10
            new_url = self.url + str(self.offset) + "#a"
            yield scrapy.Request(new_url, callback=self.parse)
```

2.items.py 文件

```
import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    people_num = scrapy.Field()
    work_address = scrapy.Field()
    publish_time = scrapy.Field()
```

*****切记字段和**TencentpositionSpider.py文件保持一致**

**3.pipelines.py文件**

```
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
```

**4.settings.py文件**

![img](https://oscimg.oschina.net/oscnet/19ca09b6a3c0dde5ccb584af04ad95aa4b8.jpg)

**5.运行文件：**

**1）在根目录下创建一个main.py**

![img](https://oscimg.oschina.net/oscnet/3c1d7af751048f1a199efc489b3e6521ce8.jpg)

2)main.py文件

```
from scrapy import cmdline

cmdline.execute("scrapy crawl tencentPosition".split())
```

**三、运行效果：**

**![img](https://img-blog.csdn.net/20180710165441807?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2EyODkyMzc2NDI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)**



```
路过的关注一下，我会继续努力的！！！！ 
```

![img](https://img-blog.csdn.net/20180713154852763?watermark/2/text/aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L2EyODkyMzc2NDI=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70)