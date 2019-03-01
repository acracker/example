#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-01 11:17
# @Author  : pang
# @File    : func_arg.py
# @Software: PyCharm

import inspect


def f(x, y, i=0, j=1, *args, **kwargs):
    return x + y + i + j


print(f.__code__.co_argcount)
print(f.__defaults__)
print(f.__code__.co_varnames)

print inspect.getargspec(f)
