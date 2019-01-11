from  bs4 import BeautifulSoup
soup = BeautifulSoup(open('scenery.html'), 'lxml')
# soup =BeautifulSoup(response.read(),exclude_encodings=['iso-8859-7', 'gb2312'])
# 排除 使其放弃不用的页面字符编码
soup.prettify()
Tag1=soup.ul

soup.ul
# 获取第一次出现ul标签的位置
soup.find('ul')
# 获取多次出现ul标签的位置【下标】
soup.find_all('ul')[0]
soup.find_all('ul')[1]
# 选择li标签里  属性相同为XX的
soup.find('li', attrs={'nu': '3'})
# 第二次出现价格的地方
Tags = soup.find_all('a', attrs={'class': 'price'})
Tags[1]
# 先间接定位 目标的上一级或者下级标签 再间接定位目标
tmpTag = soup.find('li', attrs={'nu': '2'})
tmpTag.a
tmpTag.find(a)
# 获取标签中的值 与字符串
Tag = soup.find('li', attrs={'nu': '4'})
Tag.get('nu')
Tag.a.get_text()
