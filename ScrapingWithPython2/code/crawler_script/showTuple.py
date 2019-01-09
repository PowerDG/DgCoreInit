#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'hstking hstking@hotmail.com'

class ShowTuple(object):
    def __init__(self):
        self.T1 = ()
        self.createTuple()  #创建元组
        self.subTuple(self.T1)  #元组分片
        self.tuple2List(self.T1)  #元组、列表转换

    def createTuple(self):
        print("创建元组：")
        print("T1 = (1,2,3,4,5,6,7,8,9,10)")
        self.T1 = (1,2,3,4,5,6,7,8,9,10)
        print("T1 = "),
        print(self.T1)
        print('\n')

    def subTuple(self,Tuple):
        print("元组分片：")
        print("取元组T1的第4个到最后一个元组组成的新元组，执行命令T1[3:]")
        print(self.T1[3:])
        print("取元组T1的第2个到倒数第2个元素组成的新元组，步长为2，执行命令T1[1:-1:2]")
        print(self.T1[1:-1:2])
        print('\n')

    def tuple2List(self,Tuple):
        print("元组转换成列表：")
        print("显示元组")
        print("T1 = "),
        print(self.T1)
        print("执行命令 L2 = list(T1)")
        L2 = list(self.T1)
        print("显示列表")
        print("L2 = "),
        print(L2)
        print("列表追加一个元素100后，转换成元组。执行命令L2.append(100) tuple(L2)")
        L2.append(100)
        print("显示新元组")
        print(tuple(L2))


if __name__ == '__main__':
    st = ShowTuple()
