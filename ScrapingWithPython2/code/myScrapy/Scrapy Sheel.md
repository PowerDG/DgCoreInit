(base) C:\Users\PowerDGTMS>cd /d e:



(base) E:\> cd E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy



(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy>

scrapy startproject todayMovie

scrapy startproject weather

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



(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy>

cd weather

scrapy genspider wuHanSpider wuhan.tianqi.com

cd todayMovie

cd /d E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy\todayMovie

scrapy crawl wuHanMovieSpider

---



scrapy crawl wuHanSpider

scrapy shell https://www.tianqi.com/wuhan/



scrapy shell https://www.tianqi.com/wuhan/

selector = response.xpath

Selector = response.xpath('//div[@class="day7"]')

Selector1 = Selector.xpath('ul[@class="week"]/li')

Selector1 

(base) C:\Users\PowerDg16>cd /d e:

(base) E:\>cd   E:\DgProject\PyProject\ScrapingWithPython2\code\myScrapy

(base) E:\DgProject\PyProject\ScrapingWithPython2\code\myScrapy>

cd  weather

(base) E:\DgProject\PyProject\ScrapingWithPython2\code\myScrapy\weather>

scrapy crawl wuHanSpider

scrapy crawl wuHanSpider

ls

more *.txt





(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy\todayMovie>tree todayMovie
卷 本地磁盘 的文件夹 PATH 列表
卷序列号为 C2C5-2ACA
E:\DGPROJECT\PYPROJECT\DGCOREINIT\SCRAPINGWITHPYTHON2\CODE\MYSCRAPY\TODAYMOVIE\TODAYMOVIE
├─spiders
│  └─__pycache__
└─__pycache__



(base) E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy\todayMovie>scrapy genspider wuHanMovieSpider mtime.com
Created spider 'wuHanMovieSpider' using template 'basic' in module:
  todayMovie.spiders.wuHanMovieSpider



> cd /d E:\DgProject\PyProject\DgCoreInit\ScrapingWithPython2\code\myScrapy\weather



scrapy  crawl wuHanSpider



# scrapy中 HTTP status code is not handled or not allowed异常处理

https://blog.csdn.net/u013109501/article/details/81875086

scrapy中的setting文件中添加

```
HTTPERROR_ALLOWED_CODES = [403]
```