#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = '汤小洋'

import os
import shutil

# ----操作文件和目录
print(os.path.exists('itany.txt'))  # 判断是否存在
print(os.path.abspath('itany.txt'))  # 文件的绝对路径
print(os.path.isfile('itany.txt'))  # 判断是否为文件
print(os.path.isdir('itany.txt'))  # 判断是否为目录
print(os.listdir('.'))  # 列出指定目录下所有内容
# 找出当前目录下所有的文件夹
dirs = [f for f in os.listdir('.') if os.path.isdir(f)]
print(dirs)

# 创建/删除目录
# os.mkdir('world')
if os.path.exists('world'):
    os.rmdir('world')

# 重命名文件或目录
# os.rename('itany.txt', 'aaa.txt')

# 删除文件
# os.remove('aaa.txt')

# 拷贝文件
shutil.copy('baidu.png', 'bbb.png')
