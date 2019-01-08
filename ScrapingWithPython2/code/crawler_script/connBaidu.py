#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

import urllib.request

def clear():
    '''该函数用于清屏 '''
    print('内容较多，显示3秒后翻页')
    time.sleep(3)
    OS = platform.system()
    if (OS == 'Windows'):
        os.system('cls')
    else:
        os.system('clear')

def linkBaidu():
    url = 'http://www.baidu.com'
    try:
        response = urllib.request.urlopen(url,timeout=3)
        result = response.read().decode('utf-8')
    except Exception as e:
        print("网络地址错误")
        exit()
    with open('baidu.txt', 'w') as fp:
        fp.write(result)
    print("获取url信息 : response.geturl() : %s" %response.geturl())
    print("获取返回代码 : response.getcode() : %s" %response.getcode())
    print("获取返回信息 : response.info() : %s" %response.info())
    print("获取的网页内容已存入当前目录的baidu.txt中，请自行查看")

    
if __name__ == '__main__':
    linkBaidu()
