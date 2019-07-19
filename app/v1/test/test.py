# coding: UTF-8
# author: sundapeng
# ctime: 2019-07-17 21:31
# file: test.py
# ide: PyCharm
from flask import jsonify, current_app, request
from flask_restful import Resource

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
    current_app.logger.debug('test is ok')
    return jsonify({'code': 200, 'msg': 'test is ok'})


class Test_Restful(Resource):
    '''
    测试 Restful 接口
    '''

    def get(self):
        '''
        返回所有数据
        :return:
        '''
        return jsonify({'code': 200, 'msg': 'test restful is ok'})

    def post(self):
        '''
        新增数据
        :return:
        '''
        data = request.get_json()
        return 'add new data: %s' % data
