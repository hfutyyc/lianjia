# -*- coding: utf-8 -*-
import scrapy
from ..items import LianjiaItem


class HomeSpider(scrapy.Spider):
    name = 'home_'
    allowed_domains = ['lianjia.com']
    start_urls = [
        'https://sz.lianjia.com/ershoufang/luohuqu',
        'https://sz.lianjia.com/ershoufang/futianqu',
        'https://sz.lianjia.com/ershoufang/nanshanqu',
        'https://sz.lianjia.com/ershoufang/yantianqu',
        'https://sz.lianjia.com/ershoufang/baoanqu',
        'https://sz.lianjia.com/ershoufang/longgangqu',
        'https://sz.lianjia.com/ershoufang/longhuaqu',
        'https://sz.lianjia.com/ershoufang/guangmingxinqu',
        'https://sz.lianjia.com/ershoufang/pingshanqu',
        'https://sz.lianjia.com/ershoufang/dapengxinqu',
                  ]
    headers = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    }

    def start_requests(self):
        for url in self.start_urls:
            self.headers[':path'] = url
            yield scrapy.Request(url, self.get_detail_url, headers=self.headers)

    def get_detail_url(self, response):
        urls = response.xpath('/html/body/div[3]/div/div[1]/dl[2]/dd/div[1]/div[2]//a/@href').extract()
        for url in urls:
            url = 'https://sz.lianjia.com' + url
            yield scrapy.Request(url, self.parse, headers=self.headers)

    def parse(self, response):
        # print(urls_list)
        all = response.xpath('//div[@class="resultDes clear"]/h2/span/text()').extract_first()
        all = int(int(all) / 30) + 1
        if all >= 100:
            for i in range(100):
                url = response.url + '/pg{}/'.format(i+1)
                yield scrapy.Request(url, self.get_url, headers=self.headers)
        else:
            for i in range(all):
                url = response.url + '/pg{}/'.format(i+1)
                yield scrapy.Request(url, self.get_url, headers=self.headers)

    def get_url(self, response):
        urls_list = []
        urls = response.xpath(
            '//ul[@class="sellListContent"]/li[@class="clear LOGCLICKDATA"]/div[1]/div[1]/a/@href').extract()
        # print(urls)
        for url in urls:
            urls_list.append(url)
        print(urls_list)
        for url in urls_list:
            yield scrapy.Request(url, self.parse_item, headers=self.headers)

    def parse_item(self, response):
        item = LianjiaItem()
        item['title'] = response.xpath('//div[@class="title"]/h1/text()').extract_first()
        item['total_price'] = response.xpath('//div[@class="price "]/span[1]/text()').extract_first()
        item['unit_price'] = response.xpath('//div[@class="price "]/div[1]/div[1]/span/text()').extract_first()
        item['room'] = response.xpath('//div[@class="room"]//text()').extract_first()
        item['area'] = response.xpath('//div[@class="area"]/div[1]/text()').extract_first()
        item['place'] = response.xpath('//div[@class="aroundInfo"]/div[2]/span[2]/a[1]/text()').extract_first()
        item['communityName'] = response.xpath('//div[@class="communityName"]/a[1]/text()').extract_first()

        print(item)
        yield item
