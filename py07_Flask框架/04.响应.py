#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from flask import Flask, request, redirect, jsonify
import time
import random
from flask import render_template

app = Flask(__name__)


# 响应html
@app.route('/test_html')
def test_html():
    return '''
        <h1>html</h1>
    '''


# 重定向
@app.route('/test_redirect')
def test_redirect():
    return redirect('/test_html')


# 响应json
@app.route('/test_json')
def test_json():
    user = {'id': 1001, 'name': 'tom', 'age': 18, 'sex': 'male'}
    return jsonify(user)


# 响应模板页
@app.route('/test_template')
def test_template():
    return render_template('hello.html')  # 指定模板文件名，默认在当前目录下的tempaltes中查找


if __name__ == '__main__':
    app.run(debug=True)
