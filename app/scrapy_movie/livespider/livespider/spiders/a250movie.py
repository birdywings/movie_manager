# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from ..items import Movie_Item
from .. import db,Movie_Url
from time import  sleep


class A250movieSpider(scrapy.Spider):
    name = "250movie"

    start_urls = ['http://douban.com/']



    cookies = {
    'll':"108306",
    'bid':'uo9kgAZ8zpg',
    '__yadk_uid':'bBqhdTuUTtDpKnrWURkBXCFfLy6qKI1n',
    'ps':'y',
    '_pk_ref.100001.4cf6':'%5B%22%22%2C%22%22%2C1512540651%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DGHPXaEpWKjcMeafydwwZb_7U9iDAwM9OCAHZsGB51BgocS_BNBjueFvPBMfmzAgi%26wd%3D%26eqid%3Ddb6272a30000347b000000035a1cc87f%22%5D',
    '__utmt':1,
    'ap':1,
    'as':"https://movie.douban.com/top250",
    'dbcl2':"170279666:QirJ/lYMqA0",
    'ck':'xiA6',
    '_pk_id.100001.4cf6':'01eb3a067d4f7faf.1511401610.22.1512544015.1512538644.',
    '_pk_ses.100001.4cf6':'*',
    '__utma':'30149280.1934485377.1511401610.1512537195.1512540651.22',
    '__utmb':'30149280.5.10.1512540651',
    '__utmc':'30149280',
    '__utmz':'30149280.1511947578.9.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/connect/qrconnect',
    '__utmv':'30149280.17027',
    '__utma':'223695111.625290461.1511401610.1512537195.1512540651.22',
    '__utmb':'223695111.35.10.1512540651',
    '__utmc':'223695111',
    '__utmz':'223695111.1511947578.9.3.utmcsr=open.weixin.qq.com|utmccn=(referral)|utmcmd=referral|utmcct=/connect/qrconnect',
    'push_noty_num':0,
    'push_doumail_num':0,
    '_vwo_uuid_v2':'0D66C4C42A9D5470F310A9B0C78E59C3|5926edd3ddcfa87907ad2de0b86adfed'
    }

    def parse(self, response):
        url_list = Movie_Url.query.all()

        for url in url_list:
            sleep(1)
            yield Request(url.M_Uurl, cookies=self.cookies, callback=self.parse_movie)

    def parse_movie(self, response):
        item = Movie_Item()

        name_list = response.xpath('//*[@id="content"]/h1/span[1]/text()').extract()[0].split(' ')
        item['MnameCH'] = name_list[0]
        if len(name_list) == 1  :
            item['MnameEN'] = name_list[0]
        else :
            item['MnameEN'] = ''.join(name_list[1:])

        item['Mgrade'] = response.xpath('//*[@id="interest_sectl"]/div[1]/div[2]/strong/text()').extract()[0]

        if len(response.xpath('//*[@id="info"]/span[@property="v:runtime"]/text()').extract()) > 0 :
            item['Mtime'] = response.xpath('//*[@id="info"]/span[@property="v:runtime"]/text()').extract()[0]
        else :
            item['Mtime'] = None

        item['Mdate'] = response.xpath('//*[@id="info"]/span[@property="v:initialReleaseDate"]/text()').extract()[0]
        item['Marea'] = response.xpath('//*[@id="info"]/span[8]/following::text()').extract()[0]

        picture_str = response.xpath('//*[@id="mainpic"]/a/img/@src').extract()[0]
        item['Mpicture'] = picture_str[:]

        brief_str = ''
        brief_list = response.xpath('//*[@id="link-report"]//span[@property="v:summary"]/text()').extract()
        for brief in brief_list:
            brief_str = brief_str+brief.strip('"').strip()
        item['Mbrief'] = brief_str

        type_str = ''
        for sel in response.xpath('//div[@id="info"]/span[@property="v:genre"]'):
            type_str = type_str+sel.xpath('.//text()').extract()[0]+'/'
        item['movie_type'] = type_str

        director_str = ''
        for sel in response.xpath('//div[@id="info"]/span[1]/span[@class="attrs"]'):
            director_str = director_str+sel.xpath('.//text()').extract()[0]+'/'
        item['movie_director'] = director_str

        actor_str = ''
        if len(response.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]/a').extract()) > 1:
            for value in [0,1]:
                for sel in response.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]'):
                    actor_str = actor_str+sel.xpath('./a/text()').extract()[value]+'/'
        else :
            for sel in response.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]'):
                actor_str = actor_str + sel.xpath('./a/text()').extract()[0] + '/'

        item['movie_actor'] = actor_str


        yield item
