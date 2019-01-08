# from scrapy.selector import Selector
from scrapy.selector import Selector
with open('./superHero.xml', 'r') as fp:
	body = fp.read()

Selector(text=body).xpath('/*').extract()

# print(body)
# https://blog.csdn.net/u013258415/article/details/78974665
#
# pip list可以看到scrapy包，但是import scrapy 或者 scrapy startproject xxx时，却报错 ：ImportError：DLL load failed：找不到指定的程序
# 下载好后，先用pip uninstall lxml删除掉原来lxml包，
# 再pip install D:\xxxx\lxml-3.8.0-cp36-cp36m-win_amd64.whl 安装lxml
# 这是因为有的lxml包中不包含"etree"，所以需要重新下载一个包http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml
# ---------------------
# 作者：s295472781
# 来源：CSDN
# 原文：https://blog.csdn.net/u012190454/article/details/77895840
# 版权声明：本文为博主原创文章，转载请附上博文链接！
# url="https://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml"
#
#
# pip
# https://blog.csdn.net/u013258415/article/details/78974665