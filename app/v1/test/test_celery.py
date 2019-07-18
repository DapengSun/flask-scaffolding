# coding: UTF-8
# author: sundapeng 
# ctime: 2019-07-17 21:31 
# file: test_celery.py
# ide: PyCharm
from flask import jsonify
from app.v1.test import test_blueprint, current_app
from app.celery_extensions import celery


@test_blueprint.route('/celery')
def test_celery_func():
    """
    测试celery接口
    ---
    tags:
      - 测试celery接口
    description:
        测试接口
    responses:
      200:
          description: 测试成功
          example: {'code':200,'message':'test celery is ok'}
    """
    res = test_celery_oper.delay()
    current_app.logger.debug('test celery is ok')
    return jsonify({'code': 200, 'msg': 'test celery is ok'})


@celery.task
def test_celery_oper():
    return 1 + 1
