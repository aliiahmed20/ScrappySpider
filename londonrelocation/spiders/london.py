import scrapy
from scrapy import Request
from collections import deque
import json
import re

class LondonrelocationSpider(scrapy.Spider):
    name = 'londonrelocation'
    page_number = 2
    allowed_domains = ['londonrelocation.com']
    start_urls = ['https://londonrelocation.com/properties-to-rent/']

    def parse(self, response):
        urlss= response.css('.stick-bottom a::attr(href)').extract()

        for i in range(len(urlss)) :
            yield Request(url= urlss[i],
            callback= self.parse_area)


    def parse_area(self, response):
        city = None
        try:
            city = response.url
            city = city.split('keyword=')[1]
        except:
            pass
        products = response.css("body > section > div > div > div > div")
        title = response.css("div.right-cont > div.h4-space > h4 > a::text").extract()
        price = response.css("div.right-cont > div.bottom-ic > h5::text").extract()
        for i in range(len(price)):
            if 'pcm' in price[i].lower():
                price[i] = int(price[i].replace('£','').split('pcm')[0])
            else:
                price[i] = int(price[i].replace('£','').split('pw')[0])*4

        url = response.css("div.right-cont > div.h4-space > h4 > a::attr(href)").extract()
        for i in range(len(url)):
            url[i]= "https://londonrelocation.com" + url[i]

        for i in range(len(url)):
            yield {
                'title': title[i].replace('\n',''),
                'price': price[i],
                'url' : url[i],

            }
        if city is not None:
            next_page = ("https://londonrelocation.com/our-properties-to-rent/properties/?keyword="+city+"&pageset="+ str(LondonrelocationSpider.page_number))
            if LondonrelocationSpider.page_number <=3 :
                LondonrelocationSpider.page_number += 1
                yield response.follow(next_page, callback=self.parse_area)