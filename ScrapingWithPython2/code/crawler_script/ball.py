#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

import random

class SelectBall(object):
    def __init__(self):
        self.run()

    def run(self):
        while True:
            numStr = input('输入测试的次数：')
            try:
                num = int(numStr)
            except ValueError as e:
                print('要求输入一个整数')
                continue
            else:
                break
        ball = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(num):
            n = random.randint(1,10)
            ball[n-1] += 1
        for i in range(1,11):
            print('获取第%d号球的概率为%f' %(i, ball[i-1]*1.0/num))


if __name__ == '__main__':
    SB = SelectBall()
