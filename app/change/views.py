from . import change
from .. import db
from ..models import Student,Actor,Movie,AM,DM,TM
from flask import render_template,current_app,redirect,url_for,session,abort,flash,request,make_response
from .forms import FindForm


@change.route('/change_movie',methods=['GET','POST'])
def change_movie():
    form = FindForm()
    if form.validate_on_submit() :
        if Movie.query.filter_by(MnameCH=form.name.data).first() :
            movie = Movie.query.filter_by(MnameCH=form.name.data).first()
            return redirect(url_for('main.movie',moviename=movie.MnameEN))

        elif  Movie.query.filter_by(MnameEN=form.name.data).first() :
            movie = Movie.query.filter_by(MnameEN=form.name.data).first()
            return redirect(url_for('main.movie', moviename=movie.MnameEN))

    return render_template('change/change.html',form=form)




