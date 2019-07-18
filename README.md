# Flask-scaffolding
<br>
Flask-scaffolding目的是整合常用flask模块，起到复用轮子的效果<br>

## v0.10 新功能
支持celery异步任务框架-定时任务、异步任务<br>
支持<br>


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

# 开发者交流
1215404991@qq.com<br>


