# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from datetime import datetime
from SYL.items import SylItem

class GithubspiderSpider(scrapy.Spider):
    name = 'githubspider'
    allowed_domains = ['giuhub.com']
    #start_urls = ['']

    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for repos in response.css('li.public'):
            item = SylItem()
            item['name'] = repos.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)")
            item['update_time'] = repos.xpath('.//relative-time/@datetime').extract_first()
            repositories_url = response.urljoin(repos.xpath('.//a/@href').extract_first())
            request = scrapy.Request(repositories_url,callback=self.parse_k)
            request.meta['item'] = item
            yield request
            
    def parse_k(self,response):
        #item = response.meta['item']
        for k in response.css('ul.numbers-summary'):
            item = response.meta['item']
            item['commits'] = k.xpath('./li[1]//span[@class="num text-emphasized"]/text()').re_first("\n\s*(.*)")
            item['branches'] = k.xpath('./li[2]//span[@class="num text-emphasized"]/text()').re_first('\n\s*(.*)')
            item['releases'] = k.xpath('./li[3]//span[@class="num text-emphasized"]/text()').re_first('\n\s*(.*)')
            yield item
