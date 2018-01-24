import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import openpyxl
import re

# 设置代理服务器和浏览器头部
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
 Chrome/55.0.2883.87 Safari/537.36')
# proxyInfo = {'http': '61.135.217.7'}
# proxy = urllib.request.ProxyHandler(proxyInfo)
global opener   #定义为全局
opener = urllib.request.build_opener(urllib.request.HTTPHandler)
opener.addheaders = [headers]


def getList(list):
    workbook = openpyxl.load_workbook("企业名单.xlsx")
    sheet = workbook.get_sheet_by_name("汇总")
    for i in range(2,485+1):
        list[i] = sheet["B" + str(i)].value

def getInfo(list):
    url0 = "https://www.tianyancha.com/search?key="
    strEnd = "&checkFrom=searchBox"
    str1 = r"https://www.tianyancha.com/company/\d+"
    workbook = openpyxl.load_workbook("企业名单.xlsx")      #打开文件
    sheet = workbook.get_sheet_by_name("汇总")
    for i in range(303,485+1):
        name = list[i]
        name = urllib.parse.quote(name)
        url = url0 + name + strEnd
        # print(url)
        print(i)  # 计数
        try:
            data = opener.open(url).read()
            # fhandle = open("content.html","wb")
            # fhandle.write(data)
            soup = BeautifulSoup(data,"html.parser")
            tag = soup.find("a",href=re.compile(str1))
            companyUrl = tag.attrs["href"]
            # print(companyUrl)
            # companyUrlList.append(companyUrl)
            info = getCompanyInfo(i, companyUrl)
            writeInto(info, i, sheet, workbook)
        except:
            print("未找到该企业信息")
            continue


def getCompanyInfo(i,companyUrl):
    data = opener.open(companyUrl).read()
    soup = BeautifulSoup(data, "lxml")
    tag_capital = soup.find("div",{"class": "baseinfo-module-content-value"})
    info = [0]*3
    match_capital = re.match(r"\d+",tag_capital.attrs["title"])
    capital = '0'
    if match_capital is None:
        capital = '0'
    else:
        capital = match_capital.group()
    info[0] = capital                               #注册资本
    tag_type = soup.find("td",{"colspan": "2"})
    typename = tag_type.string
    info[1] = typename                  #行业
    tag_score = soup.find("img",{"class": "td-score-img"})
    score = tag_score.attrs["alt"]
    score = re.search("\d+",score)
    if score is None:
        info[2] = '0'
    else:
        info[2] = score.group()
    print(info)
    return info

def writeInto(info, i, sheet, workbook):
    sheet["C" + str(i)] = info[1]
    sheet["D" + str(i)] = info[0]
    sheet["E" + str(i)] = info[2]
    workbook.save("企业名单.xlsx")

list = [0] * (485+1)
getList(list)
getInfo(list)

# for item in companyUrlList:
#     print(item)
# print(companyUrlList[:5])