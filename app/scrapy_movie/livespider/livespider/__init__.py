import os
from flask import Flask,render_template,session,redirect,url_for,flash #使用flask框架
from flask_script import Manager        #使用命令行管理
from flask_sqlalchemy import SQLAlchemy #引入数据库
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__) #使用flask框架

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:200020@localhost/movie'

db = SQLAlchemy(app)

class AM(db.Model):
    __tablename__ = 'am'
    actor_id = db.Column(db.Integer,db.ForeignKey('actor.Aid')
                         ,primary_key=True)

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.Mid')
                         , primary_key=True)

class DM(db.Model):
    __tablename__ = 'dm'
    director_id = db.Column(db.Integer,db.ForeignKey('director.Did')
                         ,primary_key=True)

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.Mid')
                         , primary_key=True)

class TM(db.Model):
    __tablename__ = 'tm'
    type_id = db.Column(db.Integer,db.ForeignKey('type.Tid')
                         ,primary_key=True)

    movie_id = db.Column(db.Integer, db.ForeignKey('movie.Mid')
                         , primary_key=True)


class Movie(db.Model):
    __tablename__ = 'movie'
    Mid = db.Column(db.Integer, primary_key=True)
    MnameCH = db.Column(db.String(64), unique=True)
    MnameEN = db.Column(db.String(64), unique=True)
    Mgrade = db.Column(db.String(16))
    Marea = db.Column(db.String(64))
    Mdate = db.Column(db.String(128))
    Mtime = db.Column(db.String(16))
    Mbrief = db.Column(db.Text())
    Mpicture = db.Column(db.String(128), unique=True)
    MActor = db.relationship('AM', foreign_keys=[AM.movie_id], backref=db.backref
    ('movie', lazy='joined'), lazy='dynamic', cascade='all,delete-orphan')
    MDirector = db.relationship('DM', foreign_keys=[DM.movie_id], backref=db.backref
    ('movie', lazy='joined'), lazy='dynamic', cascade='all,delete-orphan')
    Mtype = db.relationship('TM', foreign_keys=[TM.movie_id], backref=db.backref
    ('movie', lazy='joined'), lazy='dynamic', cascade='all,delete-orphan')




class Actor(db.Model):
    __tablename__ = 'actor'
    Aid = db.Column(db.Integer, primary_key=True)
    AnameCH = db.Column(db.String(64), unique=True)
    AnameEN = db.Column(db.String(64), unique=True)
    Asex = db.Column(db.String(64))
    Acome_from = db.Column(db.String(64))
    Amovie = db.relationship('AM', foreign_keys=[AM.actor_id], backref=db.backref
    ('actor', lazy='joined'), lazy='dynamic', cascade='all,delete-orphan')


class Director(db.Model):
    __tablename__ = 'director'
    Did = db.Column(db.Integer, primary_key=True)
    DnameCH = db.Column(db.String(64), unique=True)
    DnameEN = db.Column(db.String(64), unique=True)
    Dsex = db.Column(db.String(64))
    Dcome_from = db.Column(db.String(64))
    Dmovie = db.relationship('DM', foreign_keys=[DM.director_id], backref=db.backref
    ('director', lazy='joined'), lazy='dynamic', cascade='all,delete-orphan')

class Type(db.Model):
    __tablename__ = 'type'
    Tid = db.Column(db.Integer, primary_key=True)
    Tname = db.Column(db.String(64), unique=True)
    Tmovie = db.relationship('TM', foreign_keys=[TM.type_id], backref=db.backref
    ('type', lazy='joined'), lazy='dynamic', cascade='all,delete-orphan')


class Student(db.Model):
    __tablename__ = 'student'
    Sid = db.Column(db.Integer, primary_key=True)
    Sname = db.Column(db.String(64), unique=True)
    Ssex = db.Column(db.String(64))
    Sclass = db.Column(db.String(64))

class Movie_Url(db.Model) :
    __tablename__ = 'movie_url'
    M_Uid = db.Column(db.Integer, primary_key=True)
    M_Uname = db.Column(db.String(64), unique=True)
    M_Uurl = db.Column(db.String(128), unique=True)

class Actor_Url(db.Model) :
    __tablename__ = 'actor_url'
    A_Uid = db.Column(db.Integer, primary_key=True)
    A_Uname = db.Column(db.String(64), unique=True)
    A_Uurl = db.Column(db.String(128), unique=True)

class Director_Url(db.Model) :
    __tablename__ = 'director_url'
    D_Uid = db.Column(db.Integer, primary_key=True)
    D_Uname = db.Column(db.String(64), unique=True)
    D_Uurl = db.Column(db.String(128), unique=True)

