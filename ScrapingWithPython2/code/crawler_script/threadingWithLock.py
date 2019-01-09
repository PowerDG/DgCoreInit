#!/usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

import time
import threading
import codecs

def showName(threadNum ,name):
    mutex.acquire()
    with codecs.open('test.txt', 'a', 'utf-8') as fp: #写入到test.txt文件内
        nowTime = time.strftime('%H:%M:%S', time.localtime(time.time()))
        fp.write('I am thread-%d ,My name is function-%s, now time: %s\r\n ' %(threadNum, name, nowTime))
        print('I am thread-%d ,My name is function-%s, now time: %s ' %(threadNum, name, nowTime))
    mutex.release()
    time.sleep(1)


if __name__ == '__main__':
    with codecs.open('test.txt', 'w', 'utf-8') as fp:
        fp.write('')
    print('I am main ...')
    mutex = threading.Lock()
    names = [x for x in range(100)]
    threadNum = 1
    threadPool = []
    while names:
        for i in range(13):
            try:
                name = names.pop()
            except IndexError as e:
                print('The list is empty')
                break
            else:
                t = threading.Thread(target=showName, args=(i, name, ))
            threadPool.append(t)
            t.start()
        while threadPool:
            t = threadPool.pop()
            t.join()
        threadNum += 1
    print('main is over ...')


