import urllib.request
from bs4 import BeautifulSoup

def getContentUrlList(url,opener,contentUrlList):
    for pageNum in range(1,2):
        url_i = url + str(pageNum)
        data = opener.open(url).read()
        soup = BeautifulSoup(data,"html.parser")
        for tag in soup.find_all("a",{"class": "contentHerf"}):
            try:
                contentUrl = tag.attrs["href"]
                contentUrl = "https://www.qiushibaike.com" + contentUrl
                contentUrlList.append(contentUrl)
            except:
                continue


def getContent(contentUrlList,opener):
    fhandle = open("D:/Python 3.6/爬虫/糗事百科段子/段子.txt","wb")
    for contentUrl in contentUrlList:
        try:
            data = opener.open(contentUrl).read()
            soup = BeautifulSoup(data,"html.parser")
            content = soup.find("div", {"class": "content" }).string
            content = content + "\r\n\r\n"
            fhandle.write(content.encode())
        except:
            continue
    fhandle.close()

def main():
    url = "https://www.qiushibaike.com/8hr/page/"
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/55.0.2883.87 Safari/537.36')
    proxyInfo = {'http': '101.68.73.54:53281'}  # 代理可能会有dns劫持 如百度->有道
    proxy = urllib.request.ProxyHandler(proxyInfo)
    opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
    opener.addheaders = [headers]

    contentUrlList = []
    getContentUrlList(url, opener,contentUrlList)
    getContent(contentUrlList, opener)


main()

