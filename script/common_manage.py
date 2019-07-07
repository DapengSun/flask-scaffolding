# -*- coding: utf-8 -*-
from flask_script import Manager
from app.app import app

Common_manager = Manager(app)

@Common_manager.command
def test_common():
    print('test common is ok')

