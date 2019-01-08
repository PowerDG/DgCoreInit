#!/usr/bin/env python
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

import re
import urllib.request
import codecs
import time

class Todaymovie(object):
	'''获取金逸影院当日影视 '''
	def __init__(self):
		self.url = 'http://www.wandacinemas.com/'
		self.timeout = 5
		self.fileName = 'wandaMovie.txt'
		'''内部变量定义完毕 '''
		self.getmovieInfo()

	def getmovieInfo(self):
		response = urllib.request.urlopen(self.url,timeout=self.timeout)
		result = response.read().decode('utf-8')
		pattern = re.compile('<span class="icon_play" title=".*?">')
		movieList = pattern.findall(result)
		movieTitleList = map(lambda x:x.split('"')[3], movieList)
                #使用map过滤出电影标题
		with codecs.open(self.fileName, 'w', 'utf-8') as fp:
			print("Today is %s \r\n" %time.strftime("%Y-%m-%d"))
			fp.write("Today is %s \r\n" %time.strftime("%Y-%m-%d"))
			for movie in movieTitleList:
				print("%s\r\n" %movie)
				fp.write("%s \r\n" %movie)


if __name__ == '__main__':
	tm = Todaymovie()
