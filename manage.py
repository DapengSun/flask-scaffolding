# -*- coding: utf-8 -*-
from app.app import app
from flask_script import Manager, Server
# 添加自定义命令
from scripts.common_script import Common_Manager

manager = Manager(app)


def init_scripts():
    '''
    初始化自定义脚本
    :return:
    '''
    manager.add_command('runserver', Server())


@manager.command
def test():
    print('manage command test successfully')


if __name__ == '__main__':
    # 初始化自定义脚本
    init_scripts()
    manager.run()
