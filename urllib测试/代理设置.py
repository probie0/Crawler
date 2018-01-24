import urllib.request

url = 'http://www.baidu.com'
proxyInfo = {'http': '61.135.217.7'}               #代理可能会有dns劫持 如百度->有道
proxy = urllib.request.ProxyHandler(proxyInfo)
opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
data = opener.open(url).read()

fhandle = open('E:/代理设置测试.html','wb')
fhandle.write(data)
fhandle.close()
