# -*- coding: utf-8 -*-
import scrapy
from laugh.items import LaughItem
from bs4 import BeautifulSoup
import time,sys,os,re
import urllib2

class LaughSpider(scrapy.Spider):
    name = "laughPic"
    #allowed_domains = ["tp-link.net"]
    #start_urls = ['http://tp-link.net']
    def __init__(self, url):
        #super(LaughSpider,self).__init__()
        print url
        #self.start_urls = ['http://xiaohua.zol.com.cn/detail54/53179.html']
        self.start_urls = [url]
        #self.allowed_domains = 'xiaohua.zol.com.cn'
    pass

    def parse1(self, response):

        item = LaughItem()
        self.logger.info('start_urls %s', response.url)
        content = BeautifulSoup(response.text)
        item['name'] = re.sub(r'[\\/:*?"<>]','#',content.find('h1',class_="article-title").text)
        item['path']  = content.find('div',class_="article-text").find('img')['src']
        yield item
        next_sub_url = content.find('a',class_="next")['href']
        if next_sub_url:
            url = response.urljoin(next_sub_url)
            print url
            yield self.make_requests_from_url(url)

    def parse(self, response):

        item = LaughItem()
        self.logger.info('start_urls %s', response.url)
        content = BeautifulSoup(response.text)
        try:
            item['name'] = re.sub(r'[\\/:*?"<>]','#',content.find('h1',class_="article-title").text)
            item['path']  = content.find('div',class_="article-text").find('img')['src']
            yield item
        except TypeError:
            print 'TypeError  ignore!!!'
        next_sub_url = content.find('a',class_="next")['href']
        if next_sub_url:
            url = response.urljoin(next_sub_url)
            print url
            yield scrapy.Request(url, callback=self.parse)
