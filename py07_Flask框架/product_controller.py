#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

from flask import Blueprint

product = Blueprint('product', __name__)


@product.route('/product_list')
def product_list():
    return 'product_list'


@product.route('/product_add')
def product_add():
    return 'product_add'
