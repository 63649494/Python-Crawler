#爬取豆瓣书籍
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib import request
url = "http://www.douban.com/tag/%E5%B0%8F%E8%AF%B4/?focus=book" #网页地址
res = request.urlopen(url) #打开连接
response = requests.get(url)#返回http状态响应码
http_status_code = response.status_code
print(http_status_code)
soup = BeautifulSoup(res,"html.parser")
book_div = soup.find(attrs={"id":"book"})
book_a = book_div.findAll(attrs={"class":"desc"})
for book in book_a:
    print (book.string)
