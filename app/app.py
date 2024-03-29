# -*- coding: utf-8 -*-
import logging
import logging.handlers
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_sqlalchemy(app):
    '''
    注册sqlalchemy
    :param app:
    :return:
    '''
    import config.config_sqlalchemy as config_sqlalchemy
    app.config.from_object(config_sqlalchemy)
    db.init_app(app)
    app.logger.info('注册sqlalchemy模块成功')


def register_blueprint(app):
    '''
    注册蓝图
    :return:
    '''
    from app.v1.test import test_blueprint
    app.register_blueprint(test_blueprint)
    app.logger.info('注册蓝图模块成功')


def register_swagger(app):
    '''
    注册swagger
    :param app:
    :return:
    '''
    from flasgger import Swagger
    import config.config_swagger as config_swagger
    app.config.from_object(config_swagger)
    swagger_config = Swagger.DEFAULT_CONFIG
    swagger_config['title'] = config_swagger.SWAGGER_TITLE  # 配置大标题
    swagger_config['description'] = config_swagger.SWAGGER_DESC  # 配置公共描述内容
    swagger_config['host'] = config_swagger.SWAGGER_HOST  # 请求域名
    Swagger(app, config=swagger_config)
    app.logger.info('注册swagger模块成功')


def register_logger(app):
    '''
    注册日志模块
    :param app:
    :return:
    '''
    from config.config_logger import LOGGER_FORMAT as logger_fmt, LOGGER_FILE_PATH as logger_file_path, \
        LOGGER_BACKUP_COUNT as backup_count, LOGGER_WHEN as when, LOGGER_INTERVAL as interval, LOGGER_LEVEL as level

    # 日志格式化配置
    fmt = logging.Formatter(logger_fmt)

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(fmt)
    app.logger.setLevel(level)
    app.logger.addHandler(stream_handler)

    # rotating file 配置
    file_handler = logging.handlers.TimedRotatingFileHandler(
        filename=logger_file_path, when=when, interval=interval, backupCount=backup_count
    )
    file_handler.setFormatter(fmt)
    app.logger.setLevel(level)
    app.logger.addHandler(file_handler)
    app.logger.info('注册日志模块成功')


def register_celery(app):
    '''
    创建celery配置
    :param app:
    :return:
    '''
    from app.celery_extensions import celery
    import config.config_celery as config_celery
    app.config.from_object(config_celery)
    celery.init_app(app)
    app.logger.info('注册celery模块成功')


def create_app():
    '''
    创建核心对象
    :return:
    '''
    app = Flask(__name__)
    # 创建celery配置
    register_celery(app)
    # 注册日志
    register_logger(app)
    # 注册蓝图
    register_blueprint(app)
    # 注册swagger
    register_swagger(app)
    # 注册sqlalchemy
    register_sqlalchemy(app)
    return app


app = create_app()
