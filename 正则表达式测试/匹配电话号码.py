import re

pat = '\d{4}-\d{7}|\d{3}-\d{8}'
str = '021-6985452365466'
result = re.search(pat,str)

print(result)