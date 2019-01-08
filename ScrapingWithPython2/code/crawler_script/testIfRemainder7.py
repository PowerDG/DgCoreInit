#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'


def isEvenNum(num):
    if num%7 == 0:
        print("%d 可以被7整除" %num)
    else:
        print("%d 不可被7整除" %num)

if __name__ == '__main__':
    numStr = input("请输入一个整数：")
    try:
        num = int(numStr)
    except ValueError as e:
        print("输入错误，要求输入一个整数")
        exit()

    isEvenNum(num)
