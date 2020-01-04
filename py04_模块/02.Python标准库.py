#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

import sys
import os
import math
import random
from datetime import datetime, timedelta
import time

print(sys.version)  # Python版本
print(sys.platform)  # 系统平台
print(sys.argv)  # 命令行参数
print(sys.path)  # 模块搜索路径，包含了Python解析器查找模块的搜索路径
print(sys.modules)  # 显示当前程序中引入的所有模块
print(sys.getdefaultencoding())  # 默认字符集
# sys.exit('程序退出') # 退出解析器
print('---------------------------------')

print(os.name)  # 操作系统的类型
print(os.environ['path'])  # 系统的环境变量
print(os.getcwd())  # 当前的目录
print(os.listdir('d:/'))  # 列出指定目录中的内容
# os.system('ping www.baidu.com')  # 执行系统命令
print(os.path.exists('d:/soft'))  # 判断路径是否存在
print('---------------------------------')

print(math.pi)
print(math.ceil(3.4))
print(math.floor(3.4))
print(math.pow(2, 3))
print(math.trunc(2.6))  # 截尾取整
print(round(2.6))
print(round(3.1415925, 3))  # 四舍五入，保留三位小数
print('---------------------------------')

print(random.random())  # 返回[0,1)之间的随机浮点数
print(random.randint(1, 101))  # 返回[1,100]之间的随机整数
print(random.sample([1, 21, 54, 23, 6, 2], 2))  # 从数组中返回随机两个元素
print('---------------------------------')

print(datetime.now(), type(datetime.now()))  # 返回当前时间
print(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))  # 将datetime转换为指定格式的str
print(datetime.strftime(datetime.now(), '%Y{0}%m{1}%d{2} %H:%M:%S').format('年', '月', '日'))
print(datetime.strptime('2018-2-14', '%Y-%m-%d'))  # 将str转换为datetime
print('明天：', datetime.now() + timedelta(days=1))  # timedelta表示两个时间之间的时间差，可以用来进行日间的加减操作
print('前一秒：', datetime.now() - timedelta(seconds=1))
print('---------------------------------')

print(time.time())  # 返回当前时间的时间戳
print(int(time.time()))  # 秒级时间戳
print(int(time.time() * 1000))  # 毫秒时间戳
time.sleep(5)  # 休眠5秒
print(1111)
