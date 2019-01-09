#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'


import urllib.request
import re
import threading
import codecs

class TestProxy(object):
    def __init__(self):
        self.sFile = 'proxy.txt'
        self.dFile = 'alive.txt'
        self.URL = 'http://www.baidu.com/'
        self.threads = 10
        self.timeout = 3
        self.regex = re.compile('baidu.com')
        self.aliveList = []

        self.run()

    def run(self):
        with codecs.open(self.sFile, 'r', 'utf-8') as fp:
            lines = fp.readlines()
            line = lines.pop()
            while lines:
                for i in range(self.threads):
                    t = threading.Thread(target=self.linkWithProxy, args=(line,))
                    t.start()
                    if lines:
                        line = lines.pop()
                    else:
                        continue

        with codecs.open(self.dFile, 'w', 'utf-8') as fp:
            for i in range(len(self.aliveList)):
                fp.write(self.aliveList[i])



    def linkWithProxy(self, line):
        proxyStr = line.split('||')[0]
        proxyDic = eval(proxyStr)
        opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxyDic))
        urllib.request.install_opener(opener)
        try:
            response = urllib.request.urlopen(self.URL, timeout=self.timeout)
        except:
            print('%s connect failed' %proxyDic)
            return
        else:
            try:
                str = response.read().decode('utf-8')
            except:
                print('%s connect failed' %proxyDic)
                return
            if self.regex.search(str):
                print('%s connect success ..........' %proxyDic)
                self.aliveList.append(line)
                


if __name__ == '__main__':
    TP = TestProxy()
