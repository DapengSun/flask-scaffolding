# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from script.common_manage import common_manager
from script.db_manage import db_manager
from app.app import db, app
from app.v1.model import *

manager = Manager(app)
migrate = Migrate(app, db)


def register_command():
    '''
    注册命令
    :return:
    '''
    manager.add_command('common', common_manager)
    # sqlalchemy创建、迁移
    # $ python manage.py db init
    # $ python manage.py db migrate
    # $ python manage.py db upgrade
    # $ python manage.py db --help
    manager.add_command('db', MigrateCommand)
    # 启动服务
    # $ python manage.py runserver
    manager.add_command('runserver', Server(host='127.0.0.1', port=9000, use_debugger=True, use_reloader=False))


@manager.command
def test():
    return 'test command is ok'


if __name__ == '__main__':
    register_command()
    manager.run()
