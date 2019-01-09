#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'


from selenium import webdriver
from myLog import MyLog as mylog
import codecs

pageMax = 10 #爬取的页数
saveFileName = 'proxy.txt'

class Item(object):
	ip = None #代理IP地址
	port = None #代理IP端口
	anonymous = None #是否匿名
	protocol = None #支持的协议http or https
	local = None #物理位置
	speed = None #测试速度
	uptime = None #最后测试时间

class GetProxy(object):
	def __init__(self):
		self.startUrl = 'https://www.kuaidaili.com/free'
		self.log = mylog()
		self.urls = self.getUrls()
		self.proxyList = self.getProxyList(self.urls)
		self.fileName = saveFileName
		self.saveFile(self.fileName, self.proxyList)

	def getUrls(self):
		urls = []
		for word in ['inha', 'intr']:
			for page in range(1, pageMax + 1): 
				urlTemp = []
				urlTemp.append(self.startUrl)
				urlTemp.append(word)
				urlTemp.append(str(page))
				urlTemp.append('')
				url = '/'.join(urlTemp)
				urls.append(url)
		return urls


	def getProxyList(self, urls):
		proxyList = []
		item = Item()
		for url in urls:
			self.log.info('crawl page :%s' %url)
			browser = webdriver.PhantomJS()
			browser.get(url)
			browser.implicitly_wait(5)
			elements = browser.find_elements_by_xpath('//tbody/tr')
			for element in elements:
				item.ip = element.find_element_by_xpath('./td[1]').text
				item.port = element.find_element_by_xpath('./td[2]').text
				item.anonymous = element.find_element_by_xpath('./td[3]').text
				item.protocol = element.find_element_by_xpath('./td[4]').text
				item.local = element.find_element_by_xpath('./td[5]').text
				item.speed = element.find_element_by_xpath('./td[6]').text
				item.uptime = element.find_element_by_xpath('./td[7]').text
				proxyList.append(item)
				self.log.info('add proxy %s:%s to list' %(item.ip, item.port))
			browser.quit()
		return proxyList

	def saveFile(self, fileName, proxyList):
		self.log.info('add all proxy to %s' %fileName)
		with codecs.open(fileName, 'w', 'utf-8') as fp:
			for item in proxyList:
				fp.write('%s \t' %item.ip)
				fp.write('%s \t' %item.port)
				fp.write('%s \t' %item.anonymous)
				fp.write('%s \t' %item.protocol)
				fp.write('%s \t' %item.local)
				fp.write('%s \t' %item.speed)
				fp.write('%s \r\n' %item.uptime)
				

if __name__ == '__main__':
	GP = GetProxy()
