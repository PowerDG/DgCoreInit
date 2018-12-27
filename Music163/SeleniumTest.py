# -*- coding:utf-8 -*-
from selenium import webdriver
import time
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
def main(): 
    options = Options() 
    options.add_argument('-headless')
    driver = Firefox(executable_path='./geckodriver', firefox_options=options) 
    driver.get("https://www.qiushibaike.com/8hr/page/1/") 
    print(driver.page_source)
    driver.close()

     
if __name__ == '__main__':
    main()
# ---------------------
# 作者：小洋人最happy
# 来源：CSDN
# 原文：https://blog.csdn.net/u010358168/article/details/79749149
# 版权声明：本文为博主原创文章，转载请附上博文链接！
'''
前提条件：
- 本地安装Firefox浏览器
- 本地需要geckodriver驱动器文件，如果不配置环境变量的话，需要手动指定executable_path参数

与Firefox类似，双手奉上。

前提条件：
- 本地安装Chrome浏览器
- 本地需要chromedriver驱动器文件，如果不配置环境变量的话，需要手动指定executable_path参数。

Headless mode is a very useful way to run Firefox.
https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Headless_mode

'''

# driver=webdriver.Safari()