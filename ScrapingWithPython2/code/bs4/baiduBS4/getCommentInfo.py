#!/usr/bin/evn python3
#-*- coding: utf-8 -*-
'''
Created on 2016年8月9日

@author: hstking hst_king@hotmail.com
'''


import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from mylog import MyLog as mylog
import codecs


class Item(object):
    title = None    #帖子标题
    firstAuthor = None  #帖子创建者
    firstTime = None   #帖子创建时间
    reNum = None    #总回复数
    content = None  #最后回复内容
    lastAuthor = None   #最后回复者
    lastTime = None #最后回复时间
    

class GetTiebaInfo(object):
    def __init__(self,url):
        self.url = url
        self.log = mylog()
        self.pageSum = 5
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)
        
    def getUrls(self,pageSum):
        urls = []
        pns = [str(i*50) for i in range(pageSum)]
        ul = self.url.split('=')
        for pn in pns:
            ul[-1] = pn
            url = '='.join(ul)
            urls.append(url)
        self.log.info('获取URLS成功')
        return urls

    def spider(self, urls):
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            tagsli = soup.find_all('li',attrs={'class':' j_thread_list clearfix'})
            for tag in tagsli:
                item = Item()
                item.title = tag.find('a', attrs={'class':'j_th_tit'}).get_text().strip()
                item.firstAuthor = tag.find('span', attrs={'class':'frs-author-name-wrap'}).a.get_text().strip()
                item.firstTime = tag.find('span', attrs={'title':'创建时间'}).get_text().strip()
                item.reNum = tag.find('span', attrs={'title':'回复'}).get_text().strip()
                item.content = tag.find('div', attrs={'class':'threadlist_abs threadlist_abs_onlyline '}).get_text().strip()
                item.lastAuthor = tag.find('span', attrs={'class':'tb_icon_author_rely j_replyer'}).a.get_text().strip()
                item.lastTime = tag.find('span', attrs={'title':'最后回复时间'}).get_text().strip()
                items.append(item)
                self.log.info('获取标题为<<%s>>的项成功 ...' %item.title)
        return items
    
    def pipelines(self, items):
        fileName = '百度贴吧_权利的游戏.txt'#.encode('utf-8')
        with codecs.open(fileName, 'w', 'utf-8') as fp:
            for item in items:
                try:
                    fp.write('title:%s \t author:%s \t firstTime:%s \r\n content:%s \r\n return:%s \r\n lastAuthor:%s \t lastTime:%s \r\n\r\n\r\n\r\n' 
                         %(item.title, item.firstAuthor, item.firstTime, item.content, item.reNum, item.lastAuthor, item.lastTime))
                except Exception as e:
                    self.log.error('写入文件失败')
                else:
                    self.log.info('标题为<<%s>>的项输入到"%s"成功' %(item.title, fileName))

    def getResponseContent(self, url):
        '''这里单独使用一个函数返回页面返回值，是为了后期方便的加入proxy和headers等
        '''
        urlList = url.split('=')
        urlList[1] = urllib.parse.quote(urlList[1])
        url = '='.join(urlList)
        try:
            response = urllib.request.urlopen(url)
        except:
            self.log.error('Python 返回URL:%s  数据失败' %url)
        else:
            self.log.info('Python 返回URUL:%s  数据成功' %url)
            return response.read()
    

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/f?kw=权利的游戏&ie=utf-8&pn=50'
    GTI = GetTiebaInfo(url)
