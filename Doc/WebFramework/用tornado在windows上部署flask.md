# 用tornado在windows上部署flask

​                                                   2018年07月01日 22:38:03           [fardeas](https://me.csdn.net/u010501845)           阅读数：1365                                                                  

​                   

​                                                                         版权声明：Talk is cheap,show me the code.          https://blog.csdn.net/u010501845/article/details/80878342        

# 用tornado在windows上部署flask

我的开发环境：

- **Python3.5.3**
- **Flask-1.0.1**
- **tornado-5.0.2**

------

## 一、用flask开发web应用

假设你已经开发好一个web应用，站点入口文件为web.py

```python
# coding=utf-8
from flask import *
app=Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>tornado server发布成功!</h1></body></html>'

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=80)12345678910
```

## 二、安装tornado

- 方法１：在线安装

   在dos窗口运行：     pip install tornado  

- 方法2：下载whl文件离线安装

   在[Python Extension Packages for Windows](http://www.lfd.uci.edu/~gohlke/pythonlibs/)下载tornado.whl，请根据你自己的开发环境选择对应的版本。 

  在dos窗口运行：     pip install tornado-5.0.2-cp35-cp35m-win32.whl 

## 三、创建web server

在web.py同一层目录下创建文件tornado_server.py：

```python
# coding=utf-8
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from web import app

if __name__ == '__main__':
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(80)
    IOLoop.instance().start()12345678910
```

## 四、开机自动启动web server

在web.py同一层目录下创建文件“运行tornado_server.bat”

```
@echo off
cd\
D:
cd "dev\myweb"
start python tornado_server.py
exit123456
```

在控制面板搜索任务计划程序，添加基本计划任务，开机后（或者Administrator登录后）执行“运行tornado_server.bat” 
 web server启动后，在浏览器地址栏输入<http://localhost/>即可访问站点。

## 写在最后

- 用tornado部署flask的缺点：

  1.要自己写记录日志的代码

  2.web应用提供文件下载时，文件超过一定大小，就会报错（暂时没找到解决办法）     ERROR:tornado.application:Uncaught exception     MemoryError 