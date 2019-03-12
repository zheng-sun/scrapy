# -*- coding: utf-8 -*-
import scrapy


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'

    start_urls = ['http://date.jobbole.com/']

    def parse(self, response):
        for href in response.css('h3.p-tit a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(href), callback=self.parse_data)

        next_page = response.css('#pagination-next-page a::attr(href)').extract_first()
        if next_page is not None:
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)

    def parse_data(self, response):
        yield {
            'title': response.css('h1.p-tit-single::text').extract_first(),
            'release_time': response.css('p.p-meta span::text').extract_first(),
            #'city':res
        }
