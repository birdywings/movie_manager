from flask import Blueprint

change = Blueprint('change',__name__) #登记main蓝本

from . import errors,views
