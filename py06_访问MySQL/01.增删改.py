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
cursor = conn.cursor()

# 执行sql
sql = '''
    insert into t_user 
      (username,password,age,height)
    values 
      (%s,%s,%s,%s)  
'''
num = cursor.execute(sql, ['alice', '123', 18, 175.2])  # 为占位符%s赋值
print(num)

# 提交事务
conn.commit()

# 关闭资源
cursor.close()
conn.close()
