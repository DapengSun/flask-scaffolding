# coding: UTF-8
# author: sundapeng 
# ctime: 2019-07-17 21:22 
# file: config_celery.py
# ide: PyCharm

# broker是一个消息传输的中间件
CELERY_BROKER_URL = 'redis://127.0.0.1:6379/0'
# 任务执行器
CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379/1'
