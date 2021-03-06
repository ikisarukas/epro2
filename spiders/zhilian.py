# -*- coding: utf-8 -*-
from scrapy import Request
import epro2.spiders.functions as fn
import scrapy
from selenium import webdriver




class ZhilianSpider(scrapy.Spider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = ['https://jobs.zhaopin.com/']
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }
    keywork="python"

    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("spider closed")
        # self.browser.close()

    def start_requests(self):
        urls=fn.zl_starturls(self.keywork)
        for i in urls:
            yield Request(url=i,headers=self.header,meta={'cookiejar':1},callback=self.parse_index)

    def parse_index(self, response):
        # index=response.xpath("//div[@id='listContent']//a[@class='contentpile__content__wrapper__item__info']/@href").extract()
        index = response.xpath("//div[@id='listContent']//a[@class='contentpile__content__wrapper__item__info']/@href").extract()
        company= response.xpath("//div[@id='listContent']//a[@class='contentpile__content__wrapper__item__info__box__cname__title company_title']/text()").extract()
        jobs = response.xpath(
            "//div[@id='listContent']//span[@class='contentpile__content__wrapper__item__info__box__jobname__title']/@title").extract()

        for i in jobs:
            print(i)
        # with open("test.txt","a",encoding='utf-8') as fp:
        #     for i in index:
            #     print(i)
            #     i=str(i)
            #     fp.write(i)
            #     print("over")
