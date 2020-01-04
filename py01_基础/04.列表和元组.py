#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

# ---列表list
# 定义列表，使用[]
names = ['tom', 'jack', 'alice', 'mike', 'tom', 'tom']
print(names)
print(type(names))

# 获取/设置元素
print(names[1], names[:3])
names[0] = 'lucy'
print(names)

# 追加元素
names.append('zhangsan')

# 在指定位置插入元素
names.insert(1, 'lisi')

# 删除元素
names.remove('jack')

# 弹出元素
print(names.pop(0))

# 获取元素个数
print(len(names))
print(names.count('tom'))  # 统计tom出现的次数

# 可以存储不同类型的数据
names.append(25)  # 不建议
names.append(True)

print(names)
print('-' * 80)

# ------元组tuple
# 定义元组，使用()
nums = (3, 8, 13, 25, 38, 250)
print(nums)
print(type(nums))

print(nums[2], nums[-1])
print(nums[1:3])

# 解构赋值
# a = nums[0]
# b = nums[1]
# c = nums[2]
# d = nums[3]
# e = nums[4]
# f = nums[5]
a, b, c, d, e, f = nums
print(a, b, c, d, e, f)
