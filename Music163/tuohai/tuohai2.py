import csv
from selenium import webdriver

driver = webdriver.PhantomJS()
# driver = webdriver.chrome()
url = "http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"

csvDg = open("playlist.csv", "w", newline="")
writer = csv.writer(csvDg)
writer.writerow(['标题', '播放数', '链接'])

while url != 'javascript:void(0)':
    driver.get(url)
    driver.switch_to.frame("contentFrame")
    data = driver.find_element_by_id("m-pl-container").\
        find_element_by_tag_name("li")

    for i in range(len(data)):
        nb = data[i].find_element_by_class_name("nb").text
        if '万' in nb and int(nb.split('万')[0])>500:
            mak = data[i].find_element_by_css_selector("a.zbtn.znxt").\
                get_attribute("href")

csvDg.close()