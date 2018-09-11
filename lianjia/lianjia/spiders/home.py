# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import LianjiaItem


class HomeSpider(CrawlSpider):
    name = 'home'
    allowed_domains = ['lianjia.com']
    start_urls = ['https://sz.lianjia.com/ershoufang/']

    rules = (
        Rule(LinkExtractor(allow=r'ershoufang'), follow=True),
        Rule(LinkExtractor(allow=r'sz.lianjia.com/ershoufang'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        item = LianjiaItem()
        item['title'] = response.xpath('//div[@id="title"]/h1/text()').extract_first()
        item['amount'] = response.xpath('//div[@class="price"]/span[1]/text()').extract_first()
        item['unit_price'] = response.xpath('//div[@class="price"]/div[1]/div[1]/span/text()').extract_first()
        item['room'] = response.xpath('//div[@class="room"]//text()').extract_first()
        item['area'] = response.xpath('//div[@class="area"]/div[1]/text()').extract_first()
        item['place'] = response.xpath('//div[@class="aroundInfo"]/div[2]/span[2]/a[1]/text()').extract_first()
        item['communityName'] = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()

        print(item)
        yield item
