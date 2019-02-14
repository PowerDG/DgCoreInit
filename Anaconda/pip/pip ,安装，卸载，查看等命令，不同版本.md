### 转载于：

### https://www.cnblogs.com/xiexiaoxiao/p/7147920.html 



### Python和 [pycharm](https://www.baidu.com/s?wd=pycharm&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)的使用

\1. pycharm和Python 下载

​    安装后需要激活码。判断Python是否安装好了，cmd下跑: python --version

\2. 配置环python境路径，下载的时候可选，路径一个是python所在路径，还有一个是python下的Scripts,检验是否正确方法为cmd下跑: [pip](https://www.baidu.com/s?wd=pip&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd) --version,

​    这是为了pip的使用，为了安装第三方库的方便，跑命令：pip install xxx。否则的话自己上网查找 下载库包。然后python setup.py install .自带的库都在Lib下面。

​    例如[C:](https://www.baidu.com/s?wd=C%3A&tn=24004469_oem_dg&rsv_dl=gh_pl_sl_csd)\Python34;C:\Python34\Scripts 

3.在pycharm中建立项目配置选择就可以选择配置好的python.exe所在路径，第二步骤就是建立两者的联系。

### pip使用

在pyhton/scripts文件下，pip.exe pipx.exe是存在的，在CMD命令行下，pip --version 无法参看版本号，这是因为没有配置环境变量的原因。将pip.exe所在的目录配置到环境变量就OK了

 

##  使用pip安装python包

  不同版本：前面加python版本号 -m 

 如：python3 -m pip install Django==1.10.7

  

命令：

 pip install SomePackage           # latest version

 pipinstall SomePackage==1.0.4     # specificversion

 pipinstall 'SomePackage>=1.0.4'     #minimum version

 

## pip查看已安装的包

 

-  命令：pip show packagename

 

功能：查看指定的安装包信息

 

- 命令：pip list

 

功能：列出所有的安装包

 

## pip检测更新

 

命令：pip list –outdated

 

## pip升级包

命令：pip install --upgrade packagename

 

## pip卸载包

命令：pip uninstall packagename

 

PS：

经笔者[测试](http://lib.csdn.net/base/softwaretest)，使用pip卸载使用pip安装的python包时，可以完全卸载干净，但是在使用pip卸载使用python  setup.py install安装的python包时，并不能卸载干净，仍然需要手动删除先关文件。