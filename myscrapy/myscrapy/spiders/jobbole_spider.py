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
        content_list = self.contentHandle(response)

        if content_list is not None:
            content_list['title'] = response.css('h1.p-tit-single::text').extract_first()
            content_list['release_time'] = response.css('p.p-meta span::text').extract_first()
            content_list['city'] = response.css('p.p-meta span')[1].css('a::text').extract_first()
            # yield {
            #     'title': response.css('h1.p-tit-single::text').extract_first(),
            #     'release_time': response.css('p.p-meta span::text').extract_first(),
            #     'city': response.css('p.p-meta span')[1].css('a::text').extract_first(),
            #     'content': content_list
            # }
        yield content_list

    def contentHandle(self, response):
        content = response.css('.p-entry p').extract_first()
        if content is not None:
            content_list = content.split('<br>\n')

        if len(content_list) <= 1:
            return None

        details = {}
        data_key = ['birth', # 出生日期
                'height', #身高
                'weight', #体重
                'Education', #学历
                'Location', #所在城市
                'Household', #户籍
                'Native_place', #籍贯
                'Occupation',  #职业
                'income',   #收入
                'Hobby',  #兴趣爱好
                'Long-distance-love',  #是否接受异地恋
                'marry-year', #打算几年内结婚
                'word',   #一句话脱颖而出
                'about_me', #自我介绍
                ]

        count = 0
        for data in content_list:
            if count > 13:
                break
            data_rows = data.split('：')
            details[data_key[count]] = data_rows[1]
            count += 1
        return details