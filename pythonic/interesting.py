#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-08-28 18:13
# @Author  : pang
# @File    : interesting.py
# @Software: PyCharm
import random
from random import randint

def foo(x, lst=[]):
    lst.append(x)
    return lst.count(5)


# print map(lambda x, y=[]: y.append(randint(0, 9)) or y.count(5) or y, range(10))
# print map(foo, range(10))[-1]
print list(set([randint(0, 9) for i in range(10)]))