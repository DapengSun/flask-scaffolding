# -*- coding: utf-8 -*-
from flask import Flask


def create_app():
    '''
    创建核心对象
    :return:
    '''
    app = Flask(__name__)
    return app


app = create_app()
