#!/usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

import time

def showName(name):
    nowTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print('My name is function-%s, now time: %s ' %(name, nowTime))
    time.sleep(1)


if __name__ == '__main__':
    for i in range(20): #没有开多线程的情况下，执行20次操作
        showName(i)
