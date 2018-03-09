from . import delete
from .. import db
from ..models import Student,Actor,Movie,Type,Director,AM,DM,TM
from flask import render_template,current_app,redirect,url_for,session,abort,flash,request,make_response
from .forms import Delete_movie_Form,Delete_type_Form,Delete_actor_Form,Delete_director_Form

@delete.route('/delete_www',methods=['GET','POST'])
def delete_www():
    return render_template('delete/delete.html')


@delete.route('/delete_movie',methods=['GET','POST'])
def delete_movie():
    form = Delete_movie_Form()
    if form.validate_on_submit():
        if Movie.query.filter_by(MnameCH=form.name.data).first() is None:
            flash('影片不存在')
        else:
            movie = Movie.query.filter_by(MnameCH=form.name.data).first()
            am_list = AM.query.filter_by(movie_id=movie.Mid).all()
            dm_list = DM.query.filter_by(movie_id=movie.Mid).all()
            tm_list = TM.query.filter_by(movie_id=movie.Mid).all()
            for am in am_list:
                db.session.delete(am)
            for dm in dm_list:
                db.session.delete(dm)
            for tm in tm_list:
                db.session.delete(tm)
            db.session.delete(movie)
            flash('删除成功')
            return redirect(url_for('.delete_movie'))

    return render_template('delete/delete_movie.html',form=form)

@delete.route('/delete_type',methods=['GET','POST'])
def delete_type():
    form = Delete_type_Form()
    if form.validate_on_submit():
        if Type.query.filter_by(Tname=form.name.data).first() is None:
            flash('类型不存在')
        else :
            db.session.delete(Type.query.filter_by(Tname=form.name.data).first())
            flash('删除成功')
            return redirect(url_for('.delete_type'))

    return render_template('delete/delete_type.html', form=form)


@delete.route('/delete_actor',methods=['GET','POST'])
def delete_actor():
    form = Delete_actor_Form()
    if form.validate_on_submit() :
        if Actor.query.filter_by(AnameCH=form.nameCH.data,AnameEN=form.nameEN.data,
                                 Acome_from=form.come_from.data).first() is None :
            flash('演员不存在')
        else :
            db.session.delete(Actor.query.filter_by(AnameCH=form.nameCH.data,AnameEN=form.nameEN.data,
                                 Acome_from=form.come_from.data).first())
            flash('删除成功')
            return redirect(url_for('.delete_actor'))
    return render_template('delete/delete_actor.html',form=form)

@delete.route('/delete_director',methods=['GET','POST'])
def delete_director():
    form = Delete_director_Form()
    if form.validate_on_submit() :
        if Director.query.filter_by(DnameCH=form.nameCH.data, DnameEN=form.nameEN.data,Dsex=form.sex.data,
                                    Dcome_from=form.come_from.data).first() is None :
            flash('导演不存在')
        else :
            db.session.delete(Director.query.filter_by(DnameCH=form.nameCH.data, DnameEN=form.nameEN.data,Dsex=form.sex.data,
                                    Dcome_from=form.come_from.data).first())
            flash('删除成功')
            return redirect(url_for('.delete_director'))
    return render_template('delete/delete_director.html',form=form)






















