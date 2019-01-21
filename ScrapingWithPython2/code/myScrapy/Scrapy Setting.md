

---

​        

> #####  Scrapy爬虫 捕获403状态码抛出CloseSpider异常__爬虫
>
> https://yq.aliyun.com/ziliao/286802
>
> *摘要：*
> 本文讲的是Scrapy爬虫 捕获403状态码抛出CloseSpider异常__爬虫， 
> 1、爬数据的时候，有时会遇到被该网站封IP等情况，response的状态码为403，那么这时候我们希望能够抛出 CloseSpider的异常。 2、但是如scrapy官网提到的，Scrapy默认的设置是过滤掉有是过滤掉有问题的HTTP response(即response状态码不在200-300之间)。因此403的情况会被ignore掉，意思就是我们不是处理这个url ;请求的response，直接就忽略，也就是及时我们用response.status == 
> 400判断没有作用，因为只有status处于200-300的请求才会被处理。
>
>   3. 如果我们想捕获或者处理403，或者其它如404或者500
>
> ```
> 在spider的类中把403放在handle_httpstatus_list中。如下就行。
> class MySpider(CrawlSpider): handle_httpstatus_list = [403]
> 
> 或者将403放在HTTPERROR_ALLOWED_CODES设置中
> 即在settings中增加
> HTTPERROR_ALLOWED_CODES = [403]
> 
> ```
>
>

---



> ##### HTTP status code is not handled or not allowed的解决方法
>
> --
>
> ```
> /Books/>: HTTP status code is not handled or not allowed 2017-11-04 17:21:38 [scrapy.spidermiddlewares.httperror] INFO: Ignoring response <403 http://www.dmoz.org/Computers/Programming/Languages/Python /Resources/>: HTTP status code is not handled or not allowed
> --------------------- 
> 作者：幽默的荆轲君 
> 来源：CSDN 
> 原文：https://blog.csdn.net/funnyPython/article/details/78444837 
> 版权声明：本文为博主原创文章，转载请附上博文链接！
> ```
>
> 我遇到的这个问题出现在scrapy里面，解决办法是在settings里面添加
>
> HTTPERROR_ALLOWED_CODES = [403]#上面报的是403，就把403加入。
> 
> 彩蛋：
>
> scrapy默认是遵守爬虫准则的，即settings里面，ROBOTSTXT_OBEY = True
> --比如抓取百度，在https://www.baidu.com/robots.txt里，有这样的一个规范。如果遵守，比如今日头条，是不能用scrapy爬取的。这个时候需要把ROBOTSTXT_OBEY=False.也就是不遵守它的规则。
> --------------------- 
> 作者：幽默的荆轲君 
> 来源：CSDN 
> 原文：https://blog.csdn.net/funnyPython/article/details/78444837 
> 版权声明：本文为博主原创文章，转载请附上博文链接！







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