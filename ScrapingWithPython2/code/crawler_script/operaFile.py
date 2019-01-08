#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

import os

def operaFile():
	print('创建一个名字为test.txt的文件，并在其中写入Hello Python')
	print('先得保证test.txt不存在')
	os.system('rm test.txt')
	os.system('ls -l test.txt')
	print('现在再来创建文件并写入内容\n')
	fp = open('test.txt', 'w')
	fp.write('Hello Python')
	fp.close()
	print('不要忘记用close关闭文件哦')
	print('再来看看test.txt是否存在，和内容\n')
	os.system('ls -l test.txt')
	os.system('cat test.txt')
	print('\n')

	print('如何避免open文件失败的问题呢？')
	print('使用with as就可以了')
	with open('test.txt', 'r') as fp:
		st = fp.read()
	print('test.txt的内容为:%s' %st)

if __name__ == '__main__':
	operaFile()
