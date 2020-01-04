#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from flask import Flask
from py07_Flask框架.user_controller import user
from py07_Flask框架.product_controller import product

app = Flask(__name__)

# 注册蓝图
app.register_blueprint(user)
app.register_blueprint(product)

if __name__ == '__main__':
    app.run(debug=True)
