# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from ..items import Director_Item,Actor_Item,Type_Item,Movie_Url_Item
from .. import db
from time import  sleep

class MovieFromUrlSpider(scrapy.Spider):
    name = "movie_from_url"

    def __init__(self, category=None):
        self.start_urls = ['http://douban.com/']
        self.category = category
        self.cookies = {
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
        yield Request(self.category ,cookies=self.cookies, callback=self.parse_movie)


    def parse_movie(self,response):
        item = Movie_Url_Item()

        type_str = ''
        for sel in response.xpath('//div[@id="info"]/span[@property="v:genre"]'):
            type_str = type_str + sel.xpath('.//text()').extract()[0] + '/'
        item['movie_type'] = type_str

        actor_urlstr = ''
        if len(response.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]/a').extract()) > 1:
            for value in [0, 1]:
                for sel in response.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]'):
                    actor_urlstr = actor_urlstr + sel.xpath('./a/@href').extract()[value] + ' '
        else:
            for sel in response.xpath('//div[@id="info"]/span[@class="actor"]/span[@class="attrs"]'):
                actor_urlstr = actor_urlstr + sel.xpath('./a/@href').extract()[0] + ' '
        item['movie_actor_url'] = actor_urlstr



        for sel in response.xpath('//div[@id="info"]/span[1]/span[@class="attrs"]'):
            item['movie_director_url'] = sel.xpath('./a/@href').extract()[0]


        # 2. 对actor处理
        for actor_url in item['movie_actor_url'].split() :
            yield Request('https://movie.douban.com' + actor_url, cookies=self.cookies,
                          callback=self.parse_actor)

        # 3. 对director处理
        yield Request('https://movie.douban.com' + item['movie_director_url'],cookies=self.cookies,
                      callback=self.parse_director)

        # 4. 对Type处理
        yield Request('https://movie.douban.com',meta={'type_list': item['movie_type'].split('/')},
                      cookies=self.cookies, callback=self.parse_type)


    # 2. 对actor处理
    def parse_actor(self, response):
        item = Actor_Item()

        name_list = response.xpath('//*[@id="content"]/h1/text()').extract()[0].split(' ')
        item['AnameCH'] = name_list[0]
        item['AnameEN'] = ''.join(name_list[1:])
        item['Asex'] = response.xpath('//*[@id="headline"]/div[2]/ul/li[1]/text()').extract()[1].strip(':').strip()
        if len(response.xpath('//*[@id="headline"]/div[2]/ul/li[4]/text()').extract()) < 2:
            item['Acome_from'] = None
        else:
            item['Acome_from'] = response.xpath('//*[@id="headline"]/div[2]/ul/li[4]/text()').extract()[1].strip(
                ':').strip()


        item['movie_flag'] = 2
        yield item







    # 3. 对director处理
    def parse_director(self, response):
        item = Director_Item()

        name_list = response.xpath('//*[@id="content"]/h1/text()').extract()[0].split(' ')
        item['DnameCH'] = name_list[0]
        item['DnameEN'] = ''.join(name_list[1:])
        item['Dsex'] = response.xpath('//*[@id = "headline"]/div[2]/ul/li[1]/text()').extract()[1].strip(':').strip()
        if len(response.xpath('//*[@id="headline"]/div[2]/ul/li[4]/text()').extract()) < 2:
            item['Dcome_from'] = None
        else:
            item['Dcome_from'] = response.xpath('//*[@id="headline"]/div[2]/ul/li[4]/text()').extract()[1].strip(
                ':').strip()

        item['movie_flag'] = 3
        yield item




    # 4. 对Type处理
    def parse_type(self, response):
        item = Type_Item()
        item['movie_flag'] = 4
        type_list = response.meta['type_list']
        for type in type_list[:-1]:
            item['type_name'] = type
            yield item





