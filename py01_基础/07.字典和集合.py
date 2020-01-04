#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

# ----字典
# 定义dict，使用大括号{}，与js中的json很类似
scores = {'tom': 98, 'jack': 100, 'alice': 60}
print(scores)
print(type(scores))

# 获取
print(scores['jack'])
print(scores.get('alice'))

# 添加/设置
scores['lucy'] = 89
scores['tom'] = 100

# 弹出（删除）
print(scores.pop('tom'))

# 判断是否存在指定的key
print('alice' in scores)

print(scores)

# 遍历
print(scores.keys())
print(scores.values())
print(scores.items())

for k in scores.keys():
    print(k, scores[k])
print('-' * 80)

for v in scores.values():
    print(v)
print('-' * 80)

for k, v in scores.items():
    print(k, v)
print('-' * 80)

# -----set集合
# 定义set，使用大括号{}
# s = {3, 12, 5, 7, 34, 12, 3}
nums = [4, 23, 1, 23, 4, 23]
s = set(nums)  # 调用set()函数将list转换为set，去除重复值
print(s)
print(type(s))

# 添加
s.add(666)
s.add(1)

# 删除
s.remove(1)

print(s)

# 遍历
for i in s:
    print(i)

