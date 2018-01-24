import urllib.request
import urllib.error


url = 'http://blog.csdn.nt'                #偶然发现blog.csdn.ne为危险网站，且不可爬取

#version 1

# try:
#     data = urllib.request.urlopen(url).read()
# except urllib.error.HTTPError as e:
#     print(e.code)
#     print(e.reason)
# except urllib.error.URLError as e:
#     print(e.reason)


#version 2

try:
    data = urllib.request.urlopen(url).read()
except urllib.error.URLError as e:
    if hasattr(e,'code'):
        print(e.code)
    if hasattr(e,'reason'):
        print(e.reason)
