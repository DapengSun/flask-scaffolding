# coding: UTF-8
# author: sundapeng 
# ctime: 2019-07-18 20:02 
# file: db_manage.py
# ide: PyCharm
from flask_script import Manager
from app.app import db, app

db_manager = Manager(app)


@db_manager.command
def db_create():
    db.create_all()
    db.commit()
    print('create db tables')
