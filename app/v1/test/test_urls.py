# coding: UTF-8
# author: sundapeng 
# ctime: 2019-07-19 12:32 
# file: test_urls.py
# ide: PyCharm
from flask_restful import Api
from app.v1.test import test_blueprint
from app.v1.test.test import Test_Restful

test_api = Api(test_blueprint)

# 注册路由
test_api.add_resource(Test_Restful, '/test_restful')
