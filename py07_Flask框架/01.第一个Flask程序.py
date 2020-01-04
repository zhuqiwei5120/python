#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from flask import Flask

# 创建一个app，即一个Flask应用
app = Flask(__name__)


# 定义路由，类似于SpringMVC中的@RequestMapping
@app.route('/')
def hello_world():
    return '<h1 style="color:red">Hello World</h1>'


@app.route('/welcome')
def welcome():
    return 'welcome to flask'


# 启动应用
if __name__ == '__main__':
    app.run(port=8888, debug=True)
