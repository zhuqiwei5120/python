#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

import pymysql

# 定义数据库连接信息
config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': '',
    'database': 'python',
    'charset': 'utf8'
}

# 获取连接
conn = pymysql.connect(**config)

# 获取游标，相当于java中的Statement
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 可以指定cursor的类型为字典，查询结果为Dict类型

# 执行sql
sql = '''
    select
        id,username,password,age,height
    from t_user    
'''
cursor.execute(sql)

# 获取查询结果
# print(cursor.fetchone()) #　每次读取一条，返回的是元组
# print(cursor.fetchone())
# print(cursor.fetchmany(2))  #  获取多条
# print(cursor.fetchall())  # 获取所有

for u in cursor.fetchall():
    print(u['username'], u['age'])

# 关闭资源
cursor.close()
conn.close()
