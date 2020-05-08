# -*- coding: utf-8 -*-
import scrapy


class MyspdSpider(scrapy.Spider):
    name = 'myspd'
    allowed_domains = ['api.producthunt.com/v2/docs']
    start_urls = ['http://api.producthunt.com/v2/docs/']

    def parse(self, response):
        # top_header = response.css("h2::text").get()
        # response.xpath('//div[@class="api--content"]/h2/text()').extract()
        # pass

        api_data = response.css(".api--content").extract()
        print("### api_data type: ", type(api_data))
