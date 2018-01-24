# -*- coding: utf-8 -*-
import scrapy
from dangdangCrawler.items import DangdangcrawlerItem
from scrapy.http import Request

class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg3-cid10010056.html']

    def parse(self, response):
        item = DangdangcrawlerItem()
        #通过各XPATH表达式分别提取商品的名称、价格、链接、评论数等信息
        item["name"] = response.xpath("//a[@class = 'pic']/@title").extract()
        item["price"] = response.xpath("//span[@class='price_n']/text()").extract()
        item["link"] = response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"] = response.xpath("//a[@name='itemlist-review']/text()").extract()
        #提取完后返回ite
        yield item
        #通过循环自动爬取n页的数据
        n = 4
        for i in range(1,n+1):
            #通过上面的网址格式构造要爬取的地址
            url= "http://category.dangdang.com/pg" + str(n) + "-cid10010056.html"
            #通过yield返回request，并指定要爬取的网址和回调函数
            #实现自动爬取
            yield Request(url,callback=self.parse)