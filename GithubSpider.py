#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/11/2 上午 11:50
# @Author  : guolao
# @Site    :
# @File    : GithubSpider.py
# @Software: PyCharm
# @Desc    :
# @license :
# @Contact : guolaomiao@gmail.com

import scrapy


class GithubSpider(scrapy.Spider):
    name = 'shiyanlou-github'

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
