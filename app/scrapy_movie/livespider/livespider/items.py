# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item


class LivespiderItem(scrapy.Item):
    movie_name = scrapy.Field()
    movie_url = scrapy.Field()

class Actor_Url_Spider_Item(scrapy.Item):
    actor_name = scrapy.Field()
    actor_url = scrapy.Field()

class Director_Url_Spider_Item(scrapy.Item):
    director_name = scrapy.Field()
    director_url = scrapy.Field()

class Type_Item(scrapy.Item) :
    type_name = scrapy.Field()

    movie_flag = scrapy.Field()

class Actor_Item(scrapy.Item) :
    AnameCH = scrapy.Field()
    AnameEN = scrapy.Field()
    Asex = scrapy.Field()
    Acome_from = scrapy.Field()

    movie_flag = scrapy.Field()

class Director_Item(scrapy.Item) :
    DnameCH = scrapy.Field()
    DnameEN = scrapy.Field()
    Dsex = scrapy.Field()
    Dcome_from = scrapy.Field()

    movie_flag = scrapy.Field()

class Movie_Item(scrapy.Item) :

    MnameCH = scrapy.Field()
    MnameEN = scrapy.Field()
    Mgrade = scrapy.Field()
    Marea = scrapy.Field()
    Mdate = scrapy.Field()
    Mtime= scrapy.Field()
    Mbrief = scrapy.Field()
    Mpicture = scrapy.Field()
    movie_actor = scrapy.Field()
    movie_director = scrapy.Field()
    movie_type = scrapy.Field()

    movie_flag = scrapy.Field()


class Movie_Url_Item(scrapy.Item) :

    MnameCH = scrapy.Field()
    MnameEN = scrapy.Field()
    Mgrade = scrapy.Field()
    Marea = scrapy.Field()
    Mdate = scrapy.Field()
    Mtime= scrapy.Field()
    Mbrief = scrapy.Field()
    Mpicture = scrapy.Field()

    movie_actor = scrapy.Field()
    movie_director = scrapy.Field()
    movie_type = scrapy.Field()

    movie_actor_url = scrapy.Field()
    movie_director_url = scrapy.Field()

    movie_flag = scrapy.Field()





