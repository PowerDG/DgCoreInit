# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem

class TencentpositionSpider(scrapy.Spider):
    name = 'tencentPosition'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/']
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
            yield item  # 下一页的数据
            total_page = response.xpath('//div[@class="left"]/span/text()').extract()[0]
            print(total_page)
            # print(url)

            if self.offset < int(total_page):
                self.offset += 10
            new_url = self.url + str(self.offset) + "#a"

            print(new_url)
            yield scrapy.Request(new_url, callback=self.parse)


# ---------------------
# 作者：a289237642
# 来源：CSDN
# 原文：https: // blog.csdn.net / a289237642 / article / details / 80988583
# 版权声明：本文为博主原创文章，转载请附上博文链接！