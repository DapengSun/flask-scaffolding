# -*- coding: utf-8 -*-
from flask import jsonify
from . import test_blueprint


@test_blueprint.route('/')
def test_func():
    return jsonify({'code': 200, 'msg': 'test is ok'})
