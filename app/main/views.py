from . import main
from .. import db
from ..models import Student,Actor,Movie,AM,DM,TM
from flask import render_template,current_app,redirect,url_for,session,abort,flash,request,make_response
from .forms import FindForm


@main.route('/',methods=['GET','POST'])
def index():
    form = FindForm()
    if form.validate_on_submit() :
        if Movie.query.filter_by(MnameCH=form.name.data).first() :
            movie = Movie.query.filter_by(MnameCH=form.name.data).first()
            return redirect(url_for('main.movie',moviename=movie.MnameEN))

        elif  Movie.query.filter_by(MnameEN=form.name.data).first() :
            movie = Movie.query.filter_by(MnameEN=form.name.data).first()
            return redirect(url_for('main.movie', moviename=movie.MnameEN))

        else :
            flash('抱歉，并没有找你想要的')

    return render_template('index.html',form=form)


@main.route('/movie/<moviename>',methods=['GET','POST'])
def movie(moviename):
    movie = Movie.query.filter_by(MnameEN=moviename).first()
    am = AM.query.filter_by(movie=movie).all()
    dm = DM.query.filter_by(movie=movie).all()
    tm = TM.query.filter_by(movie=movie).all()
    return render_template('movie.html',movie=movie, am=am, dm=dm, tm=tm)






