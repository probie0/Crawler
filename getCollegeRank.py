import requests
from bs4 import BeautifulSoup
import bs4




def getHTMLText(url):
    try:
        r = requests.get(url,timeout = 30)
        r.raise_for_status() #如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return '产生异常'



def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3].string])


def printUnivList(ulist, num):
    print("{:^10}\t{:^6}\t{:^10}".format('排名', '学校名称', '总分'))
    for i in range(num):
        u = ulist[i]
        #print("{:^10}\t{:^6}\t{:^10}".format(u[0],u[1],u[2]))
        print(u)
    



def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    print(len(html))
    fillUnivList(uinfo, html)
    print(len(uinfo))
    printUnivList(uinfo,20)


main()