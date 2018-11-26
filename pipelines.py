# -*- coding: utf-8 -*-
import  pymysql
from epro2.settings import dbhost,user,password,db
import epro2.items as items
import

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Epro2Pipeline(object):
    def __init__(self,):
        self.conn=pymysql.connect(host=dbhost,user=user,passwd=password,db=db,use_unicode=True,charset="utf8")
    def process_item(self, item, spider):
        if(isinstance(item,items.LightnovelItem)):
            category=item['category'][0]
            title = item['title'][0]
            url = item['url'][0]
