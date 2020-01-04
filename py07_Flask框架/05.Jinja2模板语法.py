#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    name = 'tom'
    age = 81
    users = [
        {'id': 1001, 'name': 'tom', 'age': 18, 'sex': 'male'},
        {'id': 1002, 'name': 'jack', 'age': 28, 'sex': 'female'},
        {'id': 1003, 'name': 'alice', 'age': 38, 'sex': 'male'}
    ]
    return render_template('result.html', username=name, age=age, users=users)


# 全局异常处理
@app.errorhandler(404)
def error_handler(e):
    print(e)
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
