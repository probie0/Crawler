import urllib.request

url0 = 'http://www.baidu.com/s?wd='
keywd = '韦玮老师'
keywd = urllib.request.quote(keywd)
url = url0 + keywd
data = urllib.request.urlopen(url).read()

fhandle = open('D:/test4.html','wb')
fhandle.write(data)
fhandle.close()