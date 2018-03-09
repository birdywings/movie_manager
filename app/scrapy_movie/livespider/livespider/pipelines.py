# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from . import db
from . import AM,DM,TM,Movie,Type,Actor,Director
from . import Student
from . import Movie_Url,Director_Url,Actor_Url


class LivespiderPipeline(object):

    def process_item(self, item, spider):
        if spider.name == 'douban_movie' :
            if Movie_Url.query.filter_by(M_Uname=item['movie_name']).first() is None:
                db.session.add(Movie_Url(M_Uname=item['movie_name'],M_Uurl=item['movie_url']))
                db.session.commit()

        if spider.name == 'douban_actor' :
            if Actor_Url.query.filter_by(A_Uname=item['actor_name']).first() is None :
                db.session.add(Actor_Url(A_Uname=item['actor_name'],A_Uurl=item['actor_url']))
                db.session.commit()

        if spider.name == 'douban_director' :
            if Director_Url.query.filter_by(D_Uname=item['director_name']).first() is None:
                db.session.add(Director_Url(D_Uname=item['director_name'],D_Uurl=item['director_url']))
                db.session.commit()

        if spider.name == 'douban_type':
            if Type.query.filter_by(Tname=item['type_name']).first() is None :
                db.session.add(Type(Tname=item['type_name']))
                db.session.commit()

        if spider.name == '250director' :
            if Director.query.filter_by(DnameCH = item['DnameCH']).first() is None :
                db.session.add(Director(DnameCH = item['DnameCH'],DnameEN = item['DnameEN'],
                                        Dsex = item['Dsex'],Dcome_from=item['Dcome_from']))
                db.session.commit()

        if spider.name == '250actor' :
            if Actor.query.filter_by(AnameCH = item['AnameCH']).first() is None :
                db.session.add(Actor(AnameCH = item['AnameCH'],AnameEN = item['AnameEN'],
                                        Asex = item['Asex'],Acome_from=item['Acome_from']))
                db.session.commit()

        if spider.name == '250movie' :
            if Movie.query.filter_by(MnameCH = item['MnameCH']).first() is None :
                db.session.add(Movie(MnameCH = item['MnameCH'],MnameEN = item['MnameEN'],
                                     Mgrade = item['Mgrade'],Mtime = item['Mtime'],
                                     Mdate = item['Mdate'],Mbrief = item['Mbrief'],
                                     Marea = item['Marea'],Mpicture = item['Mpicture']))
                db.session.commit()


                actor_list = item['movie_actor'].split('/')
                director_list = item['movie_director'].split('/')
                type_list =  item['movie_type'].split('/')

                for actor in actor_list[0:-1] :
                    if Actor.query.filter_by(AnameCH = actor).first() is not None:
                        db.session.add(AM(actor_id = Actor.query.filter_by(AnameCH = actor).first().Aid,
                                          movie_id = Movie.query.filter_by(MnameCH = item['MnameCH']).first().Mid))

                for director in director_list[0:-1] :
                    if Director.query.filter_by(DnameCH = director).first() is not None:
                        db.session.add(DM(director_id = Director.query.filter_by(DnameCH = director).first().Did,
                                          movie_id = Movie.query.filter_by(MnameCH = item['MnameCH']).first().Mid))

                for type in type_list[0:-1] :
                    db.session.add(TM(type_id = Type.query.filter_by(Tname = type).first().Tid,
                                      movie_id = Movie.query.filter_by(MnameCH = item['MnameCH']).first().Mid))

                db.session.commit()

        if spider.name == 'movie_from_url' or 'movie_from_url_2':

            #根据yield到的item['movie_flag']标志位判断对数据进行不同处理：
            #1. 对movie处理
            #2. 对actor处理
            #3. 对director处理
            #4. 对Type处理

            if item['movie_flag'] == 1 :
                if Movie.query.filter_by(MnameCH=item['MnameCH']).first() is None:
                    db.session.add(Movie(MnameCH=item['MnameCH'], MnameEN=item['MnameEN'],
                                         Mgrade=item['Mgrade'], Mtime=item['Mtime'],
                                         Mdate=item['Mdate'], Mbrief=item['Mbrief'],
                                         Marea=item['Marea'], Mpicture=item['Mpicture']))
                    db.session.commit()

                    actor_list = item['movie_actor'].split('/')
                    director_list = item['movie_director'].split('/')
                    type_list = item['movie_type'].split('/')

                    for actor in actor_list[0:-1]:

                        db.session.add(AM(actor_id=Actor.query.filter_by(AnameCH=actor).first().Aid,
                                          movie_id=Movie.query.filter_by(MnameCH=item['MnameCH']).first().Mid))


                    for director in director_list[0:-1]:

                        db.session.add(DM(director_id=Director.query.filter_by(DnameCH=director).first().Did,
                                          movie_id=Movie.query.filter_by(MnameCH=item['MnameCH']).first().Mid))

                    for type in type_list[0:-1]:
                        if Type.query.filter_by(Tname=type).first() is not None:
                            db.session.add(TM(type_id=Type.query.filter_by(Tname=type).first().Tid,
                                              movie_id=Movie.query.filter_by(MnameCH=item['MnameCH']).first().Mid))


                    db.session.commit()

            if item['movie_flag'] == 2 :
                if Actor.query.filter_by(AnameCH=item['AnameCH']).first() is None:
                    db.session.add(Actor(AnameCH=item['AnameCH'], AnameEN=item['AnameEN'],
                                         Asex=item['Asex'], Acome_from=item['Acome_from']))
                    db.session.commit()


            if item['movie_flag'] == 3 :
                if Director.query.filter_by(DnameCH=item['DnameCH']).first() is None:
                    db.session.add(Director(DnameCH=item['DnameCH'], DnameEN=item['DnameEN'],
                                            Dsex=item['Dsex'], Dcome_from=item['Dcome_from']))
                    db.session.commit()



            if item['movie_flag'] == 4 :
                if Type.query.filter_by(Tname=item['type_name']).first() is None:
                    db.session.add(Type(Tname=item['type_name']))
                    db.session.commit()








