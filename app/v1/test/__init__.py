# -*- coding: utf-8 -*-
from flask import Blueprint
from config.config_common import API_URL_PREFIX as api_prefix, API_VERSION as api_version

test_blueprint = Blueprint('test', __name__, url_prefix='{}/{}/test'.format(api_prefix, api_version))
from app.v1.test.test import *
