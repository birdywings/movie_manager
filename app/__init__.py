from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
import sys
sys.path.append('E:\python\movie1')
from config import config
import pymysql

pymysql.install_as_MySQLdb()

db = SQLAlchemy()
bootstrap=Bootstrap()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    bootstrap.init_app(app)

    from .main import main as main_blueprint #注册main蓝本
    app.register_blueprint(main_blueprint)

    from .find import find as find_blueprint  # 注册蓝本
    app.register_blueprint(find_blueprint, url_prefix='/find')  # url前缀

    from .add import add as add_blueprint  # 注册蓝本
    app.register_blueprint(add_blueprint, url_prefix='/add')  # url前缀

    from .delete import delete as delete_blueprint  # 注册蓝本
    app.register_blueprint(delete_blueprint, url_prefix='/delete')  # url前缀

    from .change import change as change_blueprint  # 注册蓝本
    app.register_blueprint(change_blueprint, url_prefix='/change')  # url前缀

    return app


