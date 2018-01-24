import urllib.request
url = 'http://blog.csdn.net/bit_kaki/article/details/78209186'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/55.0.2883.87 Safari/537.36')
data = urllib.request.urlopen(req).read()

fhandle = open("E:/test3.html",'wb')
fhandle.write(data)
fhandle.close()
