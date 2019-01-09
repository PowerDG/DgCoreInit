#!/usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

import time
import threading

def showName(threadNum ,name):
    nowTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
    print('I am thread-%d ,My name is function-%s, now time: %s ' %(threadNum, name, nowTime))
    time.sleep(1)

if __name__ == '__main__':
    print('I am main ...')
    names = range(20)
    threadNum = 1 #threadNum 指的是线程执行的批次。
    threadPool = [] #线程池
    while names:
        for i in range(6):
            try: #这里需要考虑列表已经读取完毕的情况
                name = names.pop()
            except IndexError as e:
                print('The list is empty')
                break
            else:
                t = threading.Thread(target=showName, args=(i, name, ))
            threadPool.append(t)
            t.start()
        while threadPool: #也可以用for循环，然后清空threadPool线程池
            t = threadPool.pop()
            t.join() #使用join是为了阻塞主函数，意思是必须将t这个函数执行完毕后才能继续执行主函数
        threadNum += 1
        print('----------------------\r\n')
    print('main is over ...')

