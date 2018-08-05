# -*- coding: utf-8 -*-
import scrapy
from ..items import ProductItem


class SportsdirectTshirtSpider(scrapy.Spider):
    name = 'sportsdirect-tshirt'
    allowed_domains = ['sportsdirect.com']
    #start_urls = ['https://www.sportsdirect.com/mens/mens-t-shirts/']
    start_urls = ['https://www.sportsdirect.com/mens/mens-rugby-boots']

    def parse(self, response):
        products=response.css('.s-productthumbbox')
        for p in products:
            brand=p.css('.productdescriptionbrand::text').extract_first()
            name=p.css('.productdescriptionname::text').extract_first()
            price=p.css('.curprice::text').extract_first()
            productURL=p.css('a::attr("href")').extract_first()
            item=ProductItem()
            item['brand']=brand
            item['name']=name
            item['price']=price
            item['productURL']=productURL
            yield scrapy.Request(url=response.urljoin(productURL),callback=self.parseProduct, meta={'item' : item})
            #return
        nextPageLinkSelector=response.css('.NextLink::attr("href")')
        if nextPageLinkSelector:
            nextPageLink=nextPageLinkSelector[0].extract()
            yield scrapy.Request(url=response.urljoin(nextPageLink))
    
    def parseProduct(self, response):
        item=response.meta['item']
        imageURL=response.css('a::attr(srczoom)').extract()
        item['image_urls']=imageURL
        yield item