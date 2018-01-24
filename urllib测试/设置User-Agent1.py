import urllib.request

headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/55.0.2883.87 Safari/537.36')
url = 'http://blog.csdn.net/bit_kaki/article/details/78209186'
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()


print(data[:400])