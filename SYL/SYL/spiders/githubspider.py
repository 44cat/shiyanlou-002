# -*- coding: utf-8 -*-
import scrapy
import json
import requests
from datetime import datetime
from SYL.items import SylItem

class GithubspiderSpider(scrapy.Spider):
    name = 'githubspider'
    allowed_domains = ['giuhub.com']
    start_urls = ['']

    @property
    def start_urls(self):
        url_tmpl = 'http://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1, 5))

    def parse(self, response):
        for repos in response.css('li.public'):
            yield {
                'name': repos.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first("\n\s*(.*)"),
                'update_time': repos.xpath('.//relative-time/@datetime').extract_first()
            }
