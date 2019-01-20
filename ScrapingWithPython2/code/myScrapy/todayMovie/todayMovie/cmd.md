(base) C:\Users\PowerDGTMS>cd /d e:



(base) E:\> cd E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy



(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy>scrapy startproject todayMovie
New Scrapy project 'todayMovie', using template directory 'C:\\Anaconda3\\lib\\site-packages\\scrapy\\templates\\project', created in:
​    E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy\todayMovie



You can start your first spider with:
​    cd todayMovie
​    scrapy genspider example example.com



(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy>tree todayMovie
卷 本地磁盘 的文件夹 PATH 列表
卷序列号为 C2C5-2ACA
E:\DGPROJECT\PYPROJECT\DGCOREINIT\SCRAPINGWITHPYTHON2\CODE\MYSCRAPY\TODAYMOVIE
└─todayMovie
​    ├─spiders
​    │  └─__pycache__
​    └─__pycache__



(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy>cd todayMovie



(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy\todayMovie>tree todayMovie
卷 本地磁盘 的文件夹 PATH 列表
卷序列号为 C2C5-2ACA
E:\DGPROJECT\PYPROJECT\DGCOREINIT\SCRAPINGWITHPYTHON2\CODE\MYSCRAPY\TODAYMOVIE\TODAYMOVIE
├─spiders
│  └─__pycache__
└─__pycache__



(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy\todayMovie>

scrapy genspider wuHanMovieSpider mtime.com
Created spider 'wuHanMovieSpider' using template 'basic' in module:
  todayMovie.spiders.wuHanMovieSpider

测试请求返回

scrapy shell http://theater.mtime.com/China_Hubei_Province_Wuhan_Wuchang/4316/



```
selector = response.xpath('/html/body/script[3]/text()')[0].extract()
print(selector)
```







