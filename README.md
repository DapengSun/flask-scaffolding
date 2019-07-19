# Flask-scaffolding
![](https://img.shields.io/badge/version-0.1-green.svg) ![](https://img.shields.io/badge/build-developing-blue.svg)

Flask-scaffolding目的是整合常用flask模块，起到复用轮子的效果<br>

## v0.10 新功能
整合Celery异步任务框架-定时任务、异步任务<br>
整合SwaggerAPI文档框架<br>
整合Logger日志<br>
整合Flask Restful框架<br>


## 开发环境
MacOS 10.13.3 <br>
Flask 1.1.1 <br>
Python 3.6.3 <br>

## 下载及克隆
```
https://github.com/DapengSun/flask-scaffolding.git
git@github.com:DapengSun/flask-scaffolding.git
```

#### step1: 搭建虚拟环境virtualenv :
```
virtualenv --python==XXX(路径) env
```
#### step2: 安装requirements.txt中依赖包:
```
pip3 install -r requiremnets.txt 
```
#### step3: 使用manage启动服务
```
python manage.py runserver  
```
#### step4: 启动celery worker
 ```
路径/env/bin/celery -A celery_worker.celery worker --loglevel=info
```
#### step5: sqlalchemy创建、迁移
 ```
# sqlalchemy创建、迁移
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ python manage.py db --help
```

#### 参考文献
 ```
flask-migrate : https://flask-migrate.readthedocs.io/en/latest/
flask-restful : https://blog.51cto.com/yangrong/2294308
```

# 开发者交流
1215404991@qq.com<br>


