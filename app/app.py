# -*- coding: utf-8 -*-
from flask import Flask, jsonify


def register_route(flask_app):
    '''
    注册路由
    :return:
    '''
    @flask_app.route('/')
    def test_route():
        return jsonify({'code': 200,'msg': '测试接口'})


def create_app():
    '''
    创建flask核心app对象
    :return:
    '''
    app = Flask(__name__)

    # 注册路由
    register_route(app)
    return app


app = create_app()
