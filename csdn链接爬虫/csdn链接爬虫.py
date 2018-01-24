import urllib.request
import re
import chardet

url = "http://www.baidu.com"

patt = r"[^\\=](http://[A-Za-z0-9\\.\\/=\\?%\\-\\_\\&~`@':+!(^\\<)]+)"
proxy = urllib.request.ProxyHandler({"http": "61.135.217.7"})
opener = urllib.request.build_opener(proxy)
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/55.0.2883.87 Safari/537.36')
opener.addheaders = [headers]
htmlData = opener.open(url).read()
encoding = chardet.detect(htmlData)['encoding']              #检测网页的编码
htmlText = htmlData.decode(encoding)                     #二进制字节流解码为字符串
linkList = re.findall(patt,htmlText)

fhandle = open('D:/Python 3.6/爬虫/csdn链接爬虫/链接.txt','wb')
for link in linkList:
    link = link + '\r\n'
    fhandle.write(link.encode())
fhandle.close()

