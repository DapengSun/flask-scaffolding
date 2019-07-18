# coding: UTF-8
# author: sundapeng 
# ctime: 2019-07-18 10:34 
# file: celery_worker.py
# ide: PyCharm

'''
celery-worker 启动文件
'''

from app.app import create_app

app = create_app()
from app.celery_extensions import celery

# work启动方法
# 路径/celery -A celery_worker.celery worker --loglevel=info
# demo:
# /Users/sundapeng/Documents/project/flask-scaffolding/env/bin/celery -A celery_worker.celery worker --loglevel=info
