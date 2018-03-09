from flask import Blueprint

add = Blueprint('add',__name__) #登记main蓝本

from . import errors,views
