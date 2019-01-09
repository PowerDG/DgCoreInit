#!/usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

import time
import threading

class ShowName(threading.Thread): #这里的类名要大写，该类继承于threading.Thread类
    def __init__(self, threadNum ,name):
        threading.Thread.__init__(self) #这一步是必不可少的
        self.name = name
        self.threadNum = threadNum

    def run(self):
        nowTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
        print('I am thread-%d ,My name is function-%s, now time: %s ' %(self.threadNum, self.name, nowTime))
        time.sleep(1)

if __name__ == '__main__':
    print('I am main ...')
    names = [x for x in range(20)] 
    threadNum = 1
    threadPool = []
    while names:
        for i in range(6):
            try: #考虑线程已经读取完毕的情况
                name = names.pop()
            except IndexError as e:
                print('The List is empty')
                break
            else:
                t = ShowName(i, name) #这里调用ShowName几乎与直接调用threading.Thread是一样的。
            threadPool.append(t)
            t.start()
        while threadPool:
            t = threadPool.pop()
            t.join()
        threadNum += 1
        print('===============\r\n')
    print('main is over ...')

