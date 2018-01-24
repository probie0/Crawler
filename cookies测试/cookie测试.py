import urllib.request
import urllib.parse
import http.cookiejar

url = 'http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LAx0x'
postdata = urllib.parse.urlencode({'username': 'probie0', 'password': '150304124'}).encode('utf-8')
req = urllib.request.Request(url,postdata)
headers = ('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
  Chrome/55.0.2883.87 Safari/537.36')
cjar = http.cookiejar.CookieJar()

#opener 存储http头以及cookies
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
opener.addheaders = [headers]
file = opener.open(req)
data = file.read()
fhandle = open('E:/cookies测试.html','wb')
fhandle.write(data)
fhandle.close()

url2 = 'http://bbs.chinaunix.net/'
data2 = opener.open(url2).read()
fhandle2 = open('E:/cookies测试2.html','wb')
fhandle2.write(data2)
fhandle2.close()



