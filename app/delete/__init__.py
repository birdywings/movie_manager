from flask import Blueprint

delete = Blueprint('delete',__name__) #登记main蓝本

from . import errors,views
