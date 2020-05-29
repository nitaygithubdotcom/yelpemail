# -*- coding: utf-8 -*-
import scrapy
import re

class YelpmailSpider(scrapy.Spider):
    name = 'yelpmail'
    start_urls = ['https://www.yelp.com/biz/briggs-kitchen-bar-calgary?osq=Restaurants/']

    def parse(self, response):
        email = str(response.body)
        emails = re.findall("[a-z0-9]+@[a-z0-9]+[.]+[a-z]+", email)
        print(emails)
        uniquemail = set(emails)
        print(uniquemail)
        print(" | ".join(uniquemail))
