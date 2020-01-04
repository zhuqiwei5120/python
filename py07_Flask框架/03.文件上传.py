#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from flask import Flask, request
import time
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/load_form')
def load_form():
    return '''
        <form action="upload" method="post" enctype="multipart/form-data">
            file: <input type="file" name="file">
            <input type="submit" value="上传">
        </form>
    '''


@app.route('/upload', methods=['post'])
def upload():
    # 获取上传的文件
    file = request.files['file']
    # print(type(file)) #　FileStorage类型
    print(file.filename, len(file.read()), file.content_type)
    save_path = time.strftime('%Y%m%d%H%M%S') + str(random.randint(1, 100)) + file.filename
    file.save(save_path)
    return 'success'


if __name__ == '__main__':
    app.run(debug=True)
