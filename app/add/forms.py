from flask_wtf import FlaskForm         #引入基类
from wtforms import StringField,SubmitField,BooleanField,PasswordField,TextAreaField,SelectField,ValidationError,IntegerField #关于表单HTML标准字段
from wtforms.validators import DataRequired,Length,Regexp #引入验证函数
from ..models import Movie,Director,DM,Actor,AM,Type,TM


class Add_movie_Form(FlaskForm):
    nameCH = StringField('中文名字：', validators=[DataRequired(), Length(0, 64)])
    nameEN = StringField('英文名字：', validators=[DataRequired(), Length(0, 64)])
    actor = StringField('演员中文名字(有多个用/分割)：', validators=[DataRequired(), Length(0, 64)])
    director = StringField('导演中文名字(有多个用/分割)：', validators=[DataRequired(), Length(0, 64)])
    type = StringField('类型名字(有多个用/分割)：', validators=[DataRequired(), Length(0, 64)])
    grade = IntegerField('评分：', validators=[DataRequired()])
    area = StringField('地区：', validators=[DataRequired(), Length(0, 64)])
    date = StringField('上映时间：', validators=[DataRequired(), Length(0, 64)])
    time = StringField('影片时长：', validators=[DataRequired(), Length(0, 64)])
    picture = StringField('影片封面URL：', validators=[DataRequired()])
    brief = TextAreaField('影片简介：', validators=[DataRequired()])
    submit= SubmitField('确定')

class Add_type_Form(FlaskForm):
    name  = StringField('输入一个你要增加的类型',validators=[DataRequired(),Length(0,64)])
    submit= SubmitField('确定')

class Add_actor_Form(FlaskForm):
    nameCH = StringField('中文名字：',validators=[DataRequired(),Length(0,64)])
    nameEN = StringField('英文名字：', validators=[DataRequired(), Length(0, 64)])
    sex = StringField('性别：', validators=[DataRequired(), Length(0, 64)])
    come_from = StringField('来自：', validators=[DataRequired(), Length(0, 64)])
    submit = SubmitField('确定')

class Add_director_Form(FlaskForm):
    nameCH = StringField('中文名字：',validators=[DataRequired(),Length(0,64)])
    nameEN = StringField('英文名字：', validators=[DataRequired(), Length(0, 64)])
    sex = StringField('性别：', validators=[DataRequired(), Length(0, 64)])
    come_from = StringField('来自：', validators=[DataRequired(), Length(0, 64)])
    submit = SubmitField('确定')

class Add_movie_from_url_Form(FlaskForm) :
    url = StringField('请输入一个豆瓣电影URL：',validators=[DataRequired(),Length(0,64)])
    submit = SubmitField('确定')


