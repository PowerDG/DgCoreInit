import requests
url1='http://www.cntour.cn/'
strhtml=requests.get(url1)
# strhtml=requests.get('http://www.cntour.cn/')
# strhtml2=requests.get('http://www.cntour.cn/')
print(strhtml.text)