from flask_wtf import FlaskForm         #引入基类
from wtforms import StringField,SubmitField,BooleanField,PasswordField,TextAreaField,SelectField,ValidationError #关于表单HTML标准字段
from wtforms.validators import DataRequired,Length,Regexp #引入验证函数
from ..models import Movie,Director,DM,Actor,AM,Type,TM


class Delete_movie_Form(FlaskForm):
    name  = StringField('输入一个你要删除的影片',validators=[DataRequired(),Length(0,64)])
    submit= SubmitField('确定')

class Delete_type_Form(FlaskForm):
    name  = StringField('输入一个你要删除的类型',validators=[DataRequired(),Length(0,64)])
    submit= SubmitField('确定')

class Delete_actor_Form(FlaskForm):
    nameCH = StringField('中文名字：',validators=[DataRequired(),Length(0,64)])
    nameEN = StringField('英文名字：', validators=[DataRequired(), Length(0, 64)])
    sex = StringField('性别：', validators=[DataRequired(), Length(0, 64)])
    come_from = StringField('来自：', validators=[DataRequired(), Length(0, 64)])
    submit = SubmitField('确定')

class Delete_director_Form(FlaskForm):
    nameCH = StringField('中文名字：',validators=[DataRequired(),Length(0,64)])
    nameEN = StringField('英文名字：', validators=[DataRequired(), Length(0, 64)])
    sex = StringField('性别：', validators=[DataRequired(), Length(0, 64)])
    come_from = StringField('来自：', validators=[DataRequired(), Length(0, 64)])
    submit = SubmitField('确定')
