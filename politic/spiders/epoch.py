# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import os
os.environ["http_proxy"] = "http://u:password@proxy.internal.server.com:8080"
from politic.items import PoliticItem

class EpochSpider(scrapy.Spider):
    name = 'epoch'
    allowed_domains = ['epochtimes.com']
    start_urls = ['http://www.epochtimes.com/gb/ncid277_200.htm']     #modify according to the website url

    def parse(self, response):
        # print(response.body)

        links = response.xpath('//div[@class = "posts column"]/div[@class = "arttitle column"]/a/@href').extract()
        for url in links:
            yield Request(url, callback=self.parse_name)
        for i in range(200,400):
            page_url = 'http://www.epochtimes.com/gb/ncid277_{}.htm'.format(i)
            yield Request(page_url, callback=self.parse)

    def parse_name(self, response):
        items = PoliticItem()
        items['title'] = response.xpath('//div[@class = "large-8 medium-8 small-12 bgcolor column left"]//h1/text()').extract()[0]
        # print("!!!!!! title = ", items['title'])
        # items['time'] = response.xpath('//div[@id = "artbody"]//div[@class = "mbottom10 large-12 medium-12 small-12 columns"]/time/text()').extract()[0].split(':')[1]
        items['time'] = " ".join(response.xpath('//div[@id = "artbody"]//div[@class = "mbottom10 large-12 medium-12 small-12 columns"]/time/text()').extract_first().strip().split(" ")[1:4])
        # print("!!!!!! time = ", items['time'])
        items['label'] = " ".join(response.xpath('//div[@id = "artbody"]//div[@class = "mbottom10 large-12 medium-12 small-12 columns"]/a/text()').extract())
        # print("!!!!!! label = ", items['label'])
        items['link'] = response.url
        # print("!!!!!! link = ", items['link'])
        items['content'] = "".join(response.xpath('//div[@id = "artbody"]/p/text()').extract())
        # print("!!!!!! content = ", items['content'])

        yield items




