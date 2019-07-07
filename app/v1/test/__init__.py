# -*- coding: utf-8 -*-
from flask import Blueprint

test_blueprint = Blueprint('test', __name__, url_prefix='/test')
from app.v1.test.test import *
