import re
import requests
import openpyxl
from getHTMLText import getHTMLText

def parsePage(item_list,html):
    try:
        priceList = re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        titleList = re.findall(r'\"raw_title\"\:\".*?\"',html)
        for i in range(len(priceList)):
            price = eval(priceList[i].split(':')[1])
            title = eval(titleList[i].split(':')[1])
            item_list.append([price,title])
    except:
        print('')

# def printGoodsList(item_list):
#     for i in range(len(item_list)):
#         print(item_list[i])
#         print('\n')

def outputGoodsList(item_list):
    wb = openpyxl.Workbook()
    sheet = wb.get_active_sheet()
    sheet.title = '书包'
    for i in range(len(item_list)):
        sheet['A'+ str(i+1)] = item_list[i][0]
        sheet['B'+ str(i+1)] = item_list[i][1]
        # sheet['C'+ str(i+1)] = item_list[i][2]
    wb.save('itemList.xlsx')


def main():
    goods_name = '书包'
    depth = 3
    start_url = 'https://s.taobao.com/search?q=' + goods_name
    infoList = []
    for i in range(depth):
        try:
            url = start_url + '&s=' + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
    outputGoodsList(infoList)
    # printGoodsList(infoList)


main()
