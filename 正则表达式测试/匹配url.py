import re

pat = '[a-zA-Z]+://[^\s]*.[com|cn]'
str = "<a href= 'http://www.baidu.com'>"
result = re.search(pat, str)

print(result)

