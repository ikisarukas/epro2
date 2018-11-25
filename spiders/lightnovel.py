# -*- coding: utf-8 -*-
import scrapy
import threading
import epro2.mythread as mythread
import redis
from epro2.settings import pages
import epro2.spiders.functions as fn


class LightnovelSpider(scrapy.Spider):
    infoclass = ('news', 'novel', 'latestnovel')
    name = 'lightnovel'
    r=fn.conredis()
    allowed_domains = ['lightnovel.cn']
    start_urls = ['https://www.lightnovel.cn/forum-96-1.html',
                  'https://www.lightnovel.cn/forum-4-1.html',
                  'https://www.lightnovel.cn/forum-173-1.html']
    url = 'http://zhipin.com'
    header = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip,deflate,sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
    }

    def start_requests(self):
        infoclass=('news','latestnovel','novel')
        urlclass='lightnovel'
        print("###########开始爬取列表##########")
        t1=threading.Thread(target=fn.urltoredis,args=(self.r,infoclass,urlclass))
        t1.start()
        print('t1开始------------------')
        t1.join()
        # yield scrapy.Request(url=self.url,meta={'url':self.url}, callback=self.parse
        #               )
        t2=mythread.MyThread(fn.urlfromredis,args=(self.r,urlclass,),name='urlfromredis')
        for i in t2.get_result():
            print('iiiiiiiiiiiiiiiiiiiii=',i)
            yield scrapy.Request(url=i, meta={'url': i}, callback=self.parse
                         )

        #
        # t2.start()
        # print('t2开始------------------')
        # t2.join()





    def parse(self, response):
        msg=response.meta['url']
        print('parse url is -------',msg)

