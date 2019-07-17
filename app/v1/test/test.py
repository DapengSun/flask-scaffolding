# -*- coding: utf-8 -*-
from flask import jsonify
from app.v1.test import test_blueprint


@test_blueprint.route('/')
def test_func():
    """
    测试接口
    ---
    tags:
      - 测试接口
    description:
        测试接口
    responses:
      200:
          description: 测试成功
          example: {'code':200,'message':'test is ok'}
    """
    return jsonify({'code': 200, 'msg': 'test is ok'})
