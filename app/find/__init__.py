from flask import Blueprint

find = Blueprint('find',__name__) #登记main蓝本

from . import errors,views
