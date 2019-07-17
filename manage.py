# -*- coding: utf-8 -*-
from flask_script import Manager, Server
from script.common_manage import Common_manager
from app.app import app

manager = Manager(app)


def register_command():
    '''
    注册命令
    :return:
    '''
    manager.add_command('common', Common_manager)
    manager.add_command('runserver', Server(host='127.0.0.1', port=9000, use_debugger=True, use_reloader=False))


@manager.command
def test():
    return 'test command is ok'


if __name__ == '__main__':
    register_command()
    manager.run()
