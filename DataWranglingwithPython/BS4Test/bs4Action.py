
from bs4 import BeautifulSoup
import requests

# page = requests.get("https://www.jianshu.com/p/c5118c251e4b")

page = requests.get("http://www.enoughproject.org/take_action")
bs = BeautifulSoup(page.content)  # 解析获取响应页面源
print(bs.title)
print("-----")


def getpa():
    print(bs.find_all('a'))
    print(bs.find_all('p'))


def getchildren():
    header_children = [c for c in bs.head.children]
    print(header_children)
    navigation_bar = bs.find(id="globalNavigation")
    for d in navigation_bar.descendants:
        print(d)
    for s in d.previous_sibling:
        print(s)


ta_divs = bs.find_all("div", class_="views-row")
print(len(ta_divs))
for ta in ta_divs:
    titile_ = ta.h2
    link = ta.a
    about = ta.find_all('p')
    print(titile_, link, about)

all_data = []
for ta in ta_divs:
    data_dict = {}
    data_dict['title'] = ta.h2.get_text()
    data_dict['link'] = ta.a.get('href')
    data_dict['title'] = [p.get_text() for p in ta.find_all('p')]
    all_data.append(data_dict)
print(all_data)
#  EOF
print("-----")
