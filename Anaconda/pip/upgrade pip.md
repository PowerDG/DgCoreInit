如何将pip更新到最新版本？

只用使用命令如下就可以更新了。

python -m pip install --upgrade pip

而Anaconda更新命令为

conda install mingw libpython


感觉公式编辑器在线LateX公式编辑器挺好用的。网址为：http://www.codecogs.com/latex/eqneditor.php
--------------------- 
作者：csuzhaoqinghui 
来源：CSDN 
原文：https://blog.csdn.net/csuzhaoqinghui/article/details/53400634 
版权声明：本文为博主原创文章，转载请附上博文链接！







本文只提供本人的一些经验，不代表可以解决所有人的问题。

    pip安装软件时出现：Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-*(其中×与要安装的软件有关)
    
    比如安装pip install pyparsing==1.5.7出现以下错误： Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-WImLdR/pyparsing/
    
    解决方案
    
    sudo python -m pip install --upgrade --force pip 
    sudo pip install setuptools==33.1.1
---------------------
作者：Dongdong Bai 
来源：CSDN 
原文：https://blog.csdn.net/u011092188/article/details/64123561/ 
版权声明：本文为博主原创文章，转载请附上博文链接！







我在使用sudo pip install jupyter的时候出现了Command "python setup.py egg_info" failed with error code 1 in /tmp/pip-build-sr2_jA/distribute/这个错误，百度了好久也试了前人的很多方法，最后在stack overflow上看到了一句代码见奇效

easy_install -U setuptools

```python
easy_install -U setuptools
```

然后在执行sudo pip install jupyter竟然没有报错安装成功了
pip还不能完全取代easy_install，哈哈哈
--------------------- 
作者：Suika_Neko 
来源：CSDN 
原文：https://blog.csdn.net/u011324454/article/details/79076885 
版权声明：本文为博主原创文章，转载请附上博文链接！