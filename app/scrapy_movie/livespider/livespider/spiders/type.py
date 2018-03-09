# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from ..items import Type_Item
from .. import db,Movie_Url
from time import  sleep

class TypeSpider(scrapy.Spider):
    name = "douban_type"

    start_urls = ['https://movie.douban.com/top250']

    cookies = {
        'll': "108306",
        'bid': 'uo9kgAZ8zpg',
        '__yadk_uid': 'bBqhdTuUTtDpKnrWURkBXCFfLy6qKI1n',
        'ps': 'y',
        '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1512540651%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DGHPXaEpWKjcMeafydwwZb_7U9iDAwM9OCAHZsGB51BgocS_BNBjueFvPBMfmzAgi%26wd%3D%26eqid%3Ddb6272a30000347b000000035a1cc87f%22%5D',
        '__utmt': 1,
        'ap': 1,
        'as': "https://movie.douban.com/top250",
        'dbcl2': "170279666:QirJ/lYMqA0",
        'ck': 'xiA6',
        '_pk_id.100001.4cf6': '01eb3a067d4f7faf.1511401610.22.1512544015.1512538644.',
        '_pk_ses.100001.4cf6': '*',
        '__utma': '30149280.1934485377.1511401610.1512537195.1512540651.22',
        '__utmb': '30149280.5.10.1512540651',
        '__utmc': '30149280',
        '__utmz': '30149280.1511947578.9.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/connect/qrconnect',
        '__utmv': '30149280.17027',
        '__utma': '223695111.625290461.1511401610.1512537195.1512540651.22',
        '__utmb': '223695111.35.10.1512540651',
        '__utmc': '223695111',
        '__utmz': '223695111.1511947578.9.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/connect/qrconnect',
        'push_noty_num': 0,
        'push_doumail_num': 0,
        '_vwo_uuid_v2': '0D66C4C42A9D5470F310A9B0C78E59C3|5926edd3ddcfa87907ad2de0b86adfed'
    }

    def parse(self, response):

        url_list = Movie_Url.query.all()

        for url in url_list :
            sleep(1)
            yield Request(url.M_Uurl,cookies=self.cookies,callback=self.parse_type)

    def parse_type(self, response):
        item = Type_Item()

        for sel in response.xpath('//div[@id="info"]/span[@property="v:genre"]'):
            item['type_name'] = sel.xpath('.//text()').extract()[0]
            yield item
