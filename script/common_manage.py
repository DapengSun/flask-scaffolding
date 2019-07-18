# -*- coding: utf-8 -*-
from flask_script import Manager
from app.app import app

common_manager = Manager(app)


@common_manager.command
def test_common():
    print('test common is ok')
