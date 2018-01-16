#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-12-07 13:29
# @Author  : pang
# @File    : load_sub_class.py
# @Software: PyCharm
import os
import six
import inspect
from importlib import import_module
from pkgutil import iter_modules
from pythonic.load_subclass.base import Base


# 导入指定目录下的子类
def walk_modules(path):
    mods = []
    mod = import_module(path)
    mods.append(mod)
    if hasattr(mod, '__path__'):
        for _, subpath, ispkg in iter_modules(mod.__path__):
            fullpath = path + '.' + subpath
            if ispkg:
                mods += walk_modules(fullpath)
            else:
                submod = import_module(fullpath)
                mods.append(submod)
    return mods

sub_class_dir = "pythonic.load_subclass.sub_class"
for m in walk_modules(sub_class_dir):
    for obj in six.itervalues(vars(m)):
        if inspect.isclass(obj) and \
           issubclass(obj, Base) and \
           obj.__module__ == m.__name__:
            print obj
