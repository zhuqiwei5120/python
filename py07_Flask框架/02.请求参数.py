#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


# Get请求
@app.route('/test_get')
def test_get():
    a = request.args.get('a')
    b = request.args.get('b', default=666)
    print(a, b)
    return 'get'


@app.route('/load_form')
def load_form():
    return '''
        <form action="test_post" method="post">
            a: <input type="text" name="a"> <br>
            b: <input type="text" name="b"> <br>
            <input type="submit" value="提交">
        </form>
    '''


# Post请求
@app.route('/test_post', methods=['post', 'get'])  # 默认只接收GET请求，通过methods指定接收的请求方式
def test_post():
    a = request.form['a']
    b = request.form['b']
    print(a, b)
    return 'post'


# REST风格参数
@app.route('/test_rest/<name>/<int:id>')
def test_rest(name, id):
    print(name, id, type(id))
    return 'rest'


if __name__ == '__main__':
    app.run(debug=True)
