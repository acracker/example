#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-12 16:45
# @Author  : pang
# @File    : loop.py
# @Software: PyCharm

# 列表分组
lst = range(0, 99)
step = 10
grouped = [lst[i:i + step] for i in xrange(0, len(lst), step)]
for item in grouped:
    print item

