# from scrapy.selector import Selector
from scrapy.selector import Selector
with open('./superHero.xml', 'r') as fp:
	body = fp.read()

Selector(text = body).xpath('*/').extract()

