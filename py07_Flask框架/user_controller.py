#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from flask import Blueprint

# 创建蓝图
user = Blueprint('user', __name__)


# 定义蓝图路由
@user.route('/user_list')
def user_list():
    return 'user_list'


@user.route('/user_add')
def user_add():
    return 'user_add'
