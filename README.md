# python_newcoder_lower

##calss 1
###搭环境

    使用python版本是2.7，IDE是PyCharm，版本管理工具是git，代码放在github上https://github.com/FzhangSpace/python_newcoder_lower.git

    PyCharm需要进行简单的配置
        在File>Settings>Version Control>GitHub里面进行设置项目地址，github账号
        在File>Settings>Version Control>Git里面设置git.exe所在地址，一般在安装git路径的bin文件夹里面


    pip安装包的命令`pip install XXXX`

###简单抓取网页内容 c1_01.py
    这里用到python的两个包，需要使用pip安装一下
        `pip install requests`
        `pip install bs4`
        `pip install BeautifulSoup`
    也可以使用PyCharm安装，在File>Settings>Project:XXX>Project Interpreter里面双击pip
    然后直接在搜索框中输入包的名字
```python
#-*- encoding=UTF-8 -*-
import requests
from bs4 import BeautifulSoup

def qiushibaike():
    #得到网页的内容
    content = requests.get('http://www.qiushibaike.com').content
    #解析
    soup = BeautifulSoup(content,'html.parser')

    #查找在div里面class是content里面的内容
    for div in soup.find_all('div', {'class':'content'}):
        print div.text.strip()

if __name__ == '__main__':
    def qiushibaike()
```


###内置的模块

    随机数
```python
import random

#random.seed(1) #随机数种子

print 1, random.random()
print 2, random.randint(0, 200)
print 3, random.choice(range(0, 100))
print 4, random.sample(range(0, 100), 4)
a = range(1, 10, 1)
random.shuffle(a)   #打乱
print 5, a
```

    正则
```python
import re

str='abc123def12gh15'
p1 = re.compile('\d+')
p2 = re.compile('\d')
print p1.findall(str)
print p2.findall(str)

str = 'a1@163.com;b@gmail.com;c@qq.com'
p3 = re.compile('[\w]+@[163|qq]+\.com')
print p3.findall(str)

str = '<html><h>title</h><body>XXX</body></html>'
p4 = re.compile('<h>[^<]+</h>')
p5 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
print p4.findall(str)
print p5.findall(str)

str = 'xx2016-06-11yy'
p6 = re.compile('\d{4}-\d{2}-\d{2}')
print p6.findall(str)
```



