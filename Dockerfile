FROM daocloud.io/python:3.6

MAINTAINER Sundapeng <sundapeng@megvii.com>
RUN mkdir -p /Users/sundapeng/Documents/project/flask-scaffolding
WORKDIR /Users/sundapeng/Documents/project/flask-scaffolding

ADD ./requirements.txt /Users/sundapeng/Documents/project/flask-scaffolding/requirements.txt

RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt

ADD . /Users/sundapeng/Documents/project/flask-scaffolding

CMD python manage.py runserver