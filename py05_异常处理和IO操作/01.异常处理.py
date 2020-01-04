#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

try:
    print('try...')
    a = 5 / int('abc')
# except:  # 捕获所有异常
# except ZeroDivisionError as e:  # 捕获ZeroDivisionError异常，获取到异常对象
except (ZeroDivisionError, ValueError, Exception) as e:  # 捕获多种异常
    print('出现异常啦', e)
else:
    print('没有异常时执行')
finally:
    print('finally...')


# 自定义异常，继承自Exception(Exception类是所有异常类的父类)
class UsernameExistsException(Exception):
    pass


def fn(username):
    if username == 'admin' or username == 'tom':
        raise UsernameExistsException('用户名已存在')  # 使用raise抛出异常
    else:
        print('ok')


fn(input('请输入用户名：'))
