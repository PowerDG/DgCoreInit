from urllib.request import urlopen
# import beautifulsoup4
from bs4  import BeautifulSoup

# html = urlopen("http://www.runoob.com/python3/python3-iterator-generator.html")

html = urlopen("https://music.163.com/#/user/follows?id=251083240")
# https://music.163.com/#/user/follows?id=251083240

# print(html.read())
bs_Obj = BeautifulSoup(html.read(), "html.parser")
text_List = bs_Obj.find_all("a")
for text in text_List:
    print(text.get_text())
html.close()

