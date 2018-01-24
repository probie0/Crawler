import urllib.request
import  urllib.parse

url = 'http://www.iqianyue.com/mypost/'
formData = {'name':'root','pass':'1234'}
postData = urllib.parse.urlencode(formData).encode('utf-8')
req = urllib.request.Request(url,postData)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/55.0.2883.87 Safari/537.36')
data = urllib.request.urlopen(req).read()
fhandle = open('E:/post测试.html','wb')
fhandle.write(data)
fhandle.close()
