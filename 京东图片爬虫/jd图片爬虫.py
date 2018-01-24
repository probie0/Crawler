import urllib.request
from bs4 import BeautifulSoup

url = 'https://list.jd.com/list.html?cat=9987,653,655&page='

count = 0

def crawlPerPage(pageNum):
    proxy = urllib.request.ProxyHandler({"http":"114.235.82.135"})
    opener = urllib.request.build_opener(proxy)
    headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
     Chrome/55.0.2883.87 Safari/537.36')
    opener.addheaders = [headers]
    urli = url + str(pageNum)
    htmlText = opener.open(urli).read()
    soup = BeautifulSoup(htmlText,'html.parser')
    global count
    for tag in soup.find_all('img', {'width': '220', 'height': '220', 'data-img': '1'}):
        imageUrl = ''
        try:
            if 'data-lazy-img' in tag.attrs.keys():
                imageUrl = tag.attrs['data-lazy-img']
            else:
                imageUrl = tag.attrs['src']
            count = count + 1
        except:
            continue

        print(imageUrl)
        imageUrl = "http:" + imageUrl
        imageName = "D:/Python 3.6/爬虫/京东图片爬虫/爬取的图片/" + str(count) + '.jpg'
        urllib.request.urlretrieve(imageUrl,imageName)

for i in range(1,3):
    crawlPerPage(i)

print(count)



