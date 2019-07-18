# Flask-scaffolding
![](https://img.shields.io/badge/version-0.1-green.svg) ![](https://img.shields.io/badge/build-developing-blue.svg)

Flask-scaffolding目的是整合常用flask模块，起到复用轮子的效果<br>

## v0.10 新功能
整合Celery异步任务框架-定时任务、异步任务<br>
整合SwaggerAPI文档框架<br>
整合Logger日志<br>


## 开发环境
macOS 10.13.3 flask 1.1.1 python 3.6.3<br>

## 下载及克隆
```
git clone https://github.com/guohongze/adminset.git
```

#### step1: 搭建虚拟环境virtualenv :
```
virtualenv --python==XXX(路径) env
```
#### step2: 安装requirements,txt中依赖包:
```
pip3 install -r requiremnets.txt 
```
#### step3: 使用mange启动服务
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

# 开发者交流
1215404991@qq.com<br>


