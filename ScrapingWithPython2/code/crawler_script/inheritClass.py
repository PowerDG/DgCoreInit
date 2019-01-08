#!/usr/bin/env python3
#-*- coding:utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

class Ape(object): #猿猴
    '''以猿猴形态时，手、腿、眼睛的数量 '''
    eyes = 2 #这几个变量是类保护变量，是可以“遗传”给子类的。
    arms = 0 
    legs = 4 

    def __init__(self):
        '''__init__函数一般最主要的作用就是初始化 '''
        self.name = 'ape'
        self.show()

    def show(self):
        print("I am a %s" %self.name)
        print("I have %d eyes" %self.eyes)
        print("I have %d arms" %self.arms)
        print("I have %d legs" %self.legs)
        print("###### The show is over #####\r\n") #这是使用\r\n作为分段符是为了兼容Widnows


class Homohabilis(Ape): #能人
    '''能人还是用4条腿走路 '''
    def __init__(self):
        self.name = 'Homohablilis' 
        self.show()


class Homoerectus(Homohabilis): #直立人
    '''直立人用两腿走路，解放了双手 '''
    arms = 2 #这里重载了手和腿的数量
    legs = 2

    def __init__(self):
        self.name = 'Homoerectus'
        self.show()
    

class Homosapiens(Homoerectus): #智人
    '''智人也是用双腿走路，直立行走 '''
    def __init__(self):
        self.name = 'Homosapiens'
        self.show()


if __name__ == '__main__':
    ape = Ape()
    homohabilis = Homohabilis()
    homoerectus = Homoerectus()
    homosapiens = Homosapiens()
