# -*- coding: utf-8 -*-
import scrapy


class PortalSpider(scrapy.Spider):
    name = 'portal'
    allowed_domains = ['http://www.portaltransparencia.gov.br/']
    start_urls = ['http://http://www.portaltransparencia.gov.br//']

    def parse(self, response):
        pass
