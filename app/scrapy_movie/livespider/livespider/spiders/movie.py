# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from ..items import LivespiderItem
from .. import db,Movie_Url
from time import  sleep


class MovieSpider(scrapy.Spider):
    name = "douban_movie"

    start_urls = ['https://movie.douban.com/top250']


    def parse(self, response):
        item = LivespiderItem()

        for sel in response.xpath('//ol[@class="grid_view"]/li') :
            item['movie_name'] = sel.xpath('.//div[@class="hd"]/a/span[1]/text()').extract()[0]
            item['movie_url'] = sel.xpath('.//div[@class="hd"]/a/@href').extract()[0]
            yield item

        next_url = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_url:
            next_url = 'https://movie.douban.com/top250' + next_url[0]
            yield Request(next_url)
