from . import add
from .. import db
from ..models import Student,Actor,Movie,Type,Director,AM,DM,TM
from flask import render_template,current_app,redirect,url_for,session,abort,flash,request,make_response
from .forms import Add_movie_Form,Add_type_Form,Add_actor_Form,Add_director_Form,Add_movie_from_url_Form
import os,sys


@add.route('/add_www',methods=['GET','POST'])
def add_www():
    return render_template('add/add.html')

@add.route('/add_movie',methods=['GET','POST'])
def add_movie():
    form = Add_movie_Form()
    if form.validate_on_submit():
        if Movie.query.filter_by(MnameCH=form.nameCH.data,MnameEN=form.nameEN.data).first() :
            flash('影片已经存在')
        else :
            movie = Movie(MnameCH=form.nameCH.data,MnameEN=form.nameEN.data,Mgrade=form.grade.data,
                                 Marea=form.area.data,Mdate=form.date.data,Mtime=form.time.data,
                                 Mpicture=form.picture.data,Mbrief=form.brief.data)
            db.session.add(movie)
            db.session.commit()
            actor_list = form.actor.data.split('/')
            director_list = form.director.data.split('/')
            type_list = form.type.data.split('/')
            for actor in actor_list :
                # db.session.add(AM(movie_id=movie.Mid,actor_id=Actor.query.filter_by(AnameCH=actor.strip()).first().Aid))
                db.session.add(AM(movie_id=movie.Mid,actor_id=Actor.query.filter_by(AnameCH=actor).first().Aid))
            for director in director_list :
                db.session.add(DM(movie_id=movie.Mid,director_id=Director.query.filter_by(DnameCH=director).first().Did))
            for type in type_list :
                db.session.add(TM(movie_id=movie.Mid,type_id=Type.query.filter_by(Tname=type).first().Tid))
            db.session.commit()
            flash('添加成功')
            return redirect(url_for('.add_movie'))

    return render_template('add/add_movie.html',form=form)

@add.route('/add_type',methods=['GET','POST'])
def add_type():
    form = Add_type_Form()
    if form.validate_on_submit():
        if Type.query.filter_by(Tname=form.name.data).first():
            flash('类型已经存在')
        else :
            db.session.add(Type(Tname=form.name.data))
            db.session.commit()
            flash('添加成功')
            return redirect(url_for('.add_type'))

    return render_template('add/add_type.html', form=form)

@add.route('/add_actor',methods=['GET','POST'])
def add_actor():
    form = Add_actor_Form()
    if form.validate_on_submit() :
        if Actor.query.filter_by(AnameCH=form.nameCH.data,AnameEN=form.nameEN.data,
                                 Acome_from=form.come_from.data).first() :
            flash('演员已经存在')
        else :
            db.session.add(Actor(AnameCH=form.nameCH.data,AnameEN=form.nameEN.data,Asex=form.sex.data,
                                 Acome_from=form.come_from.data))
            db.session.commit()
            flash('添加成功')
            return redirect(url_for('.add_actor'))

    return render_template('add/add_actor.html', form=form)





@add.route('/add_director',methods=['GET','POST'])
def add_director():
    form = Add_director_Form()
    if form.validate_on_submit():
        if Director.query.filter_by(DnameCH=form.nameCH.data, DnameEN=form.nameEN.data,Dsex=form.sex.data,
                                    Dcome_from=form.come_from.data).first():
            flash('导演已经存在')
        else:
            db.session.add(Director(DnameCH=form.nameCH.data, DnameEN=form.nameEN.data, Dsex=form.sex.data,
                                    Dcome_from=form.come_from.data))
            db.session.commit()
            flash('添加成功')
            return redirect(url_for('.add_director'))

    return render_template('add/add_director.html', form=form)

@add.route('/add_movie_from_url',methods=['GET','POST'])
def add_movie_from_url():
    form = Add_movie_from_url_Form()
    if form.validate_on_submit():
        url = form.url.data

        print(os.getcwd())
        # 切换路径执行spider
        os.chdir('E:\python\movie1\\app\scrapy_movie\livespider\livespider')
        print(os.getcwd())

        # 导入模块，不然会出错
        sys.path.append('E:\python\movie1\config.py')
        sys.path.append('E:\python\movie1\\app')

        from app.scrapy_movie.livespider.handle_douban_url import handle_douban_url
        handle_douban_url(url)

        flash('添加成功')
        return redirect(url_for('.add_movie_from_url'))

    return render_template('add/add_movie_from_url.html',form=form)
































