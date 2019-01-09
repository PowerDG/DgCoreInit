#!/usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

from resource import userAgentList
import random
import urllib.request
import codecs

class ConnBase(object):
    '''这是一个用于返回html源代码的类'''
    accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    accept_language = 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2'
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',#Chrome
    charset = 'utf-8' #一般来说网页使用的都是utf-8码
    headers = {
        'Accept': accept,
        'Accept-Language': accept_language,
        'User-Agent': user_agent
    }
    timeout = 10

    def __init__(self, url):
        self.url = url
        self.result = self.getResponse()
        self.save2file()

    def getResponse(self, proxy={}):
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)

        opener.headers = self.headers
        urllib.request.install_opener(opener)
        try:
            req = urllib.request.Request(self.url)
            response = urllib.request.urlopen(req, timeout=self.timeout)
            result = response.read().decode(self.charset, 'ignore')
        except Exception as e:
            print(e)
            return None
        else:
            return result

    def save2file(self):
        with codecs.open(self.charset + '.txt', 'w', 'utf-8') as fp:
            fp.write(self.result)


class GetHtmlCode(ConnBase):
    ''' 继承与ConnBase基类，重载了charset变量，用于连接字符集为gbk的网站。'''
    def __init__(self, url):
        self.url = url
        self.user_agent = random.choice(userAgentList) #这里将从userAgent列表中随机挑选User-Agent，避免反爬虫干扰
        self.charset = 'gbk' #对应某些中文网站的字符编码，如果是繁体中文，一般是Gig5

        self.result = self.getResponse()
        self.save2file()


if __name__ == '__main__':
    res1 = ConnBase('http://www.linuxdiyf.com')
    res2 = GetHtmlCode('http://www.linuxdiyf.com')
