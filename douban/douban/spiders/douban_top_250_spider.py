# -*- coding: utf-8 -*-
import scrapy


class DoubanTop250SpiderSpider(scrapy.Spider):
    name = 'douban_top_250_spider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        #response.css
        for item in response.css('.item'):
            yield {
                'serial_number': item.css('em::text').extract_first(),
                'title': item.css('.title::text').extract_first(),
                'rating_num': item.css('.rating_num::text').extract_first(),
                'comment': response.css('.star span::text')[3].extract(),
                'desc': item.css('.inq::text').extract_first(),
            }

        next_page = response.css('span.next a::attr(href)').extract_first()
        print(next_page)
        if next_page is not None:
            print(response.urljoin(next_page))
            yield scrapy.Request(response.urljoin(next_page), callback=self.parse)
