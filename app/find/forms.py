from flask_wtf import FlaskForm         #引入基类
from wtforms import StringField,SubmitField,BooleanField,PasswordField,TextAreaField,SelectField,ValidationError #关于表单HTML标准字段
from wtforms.validators import DataRequired,Length,Regexp #引入验证函数
from ..models import Movie,Director,DM,Actor,AM,Type,TM


class FindForm(FlaskForm):
    name  = StringField('输入一个你要查找的影片名字',validators=[DataRequired(),Length(0,64)])
    submit= SubmitField('确定')


