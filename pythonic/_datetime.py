#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-15 11:01
# @Author  : pang
# @File    : _datetime.py
# @Software: PyCharm
import time
import datetime


curr_date = "20170615"
curr_time = datetime.datetime.now().strptime(curr_date, "%Y%m%d")
n = 5
for i in range(1, n+1):
    print (curr_time + datetime.timedelta(days=i)).strftime('%Y%m%d')