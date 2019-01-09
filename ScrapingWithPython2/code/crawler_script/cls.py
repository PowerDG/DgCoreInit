#!/usr/bin/env python3
#-*- coding: utf-8 -*-
__author__ = 'hstking hst_king@hotmail.com'

import platform
import os

def clear():
	OS = platform.system()
	if OS == 'Windows':
		os.system('cls')
	else:
		os.system('clear')



if __name__ == '__main__':
	pass
