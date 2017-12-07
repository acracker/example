#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-07-07 10:06
# @Author  : pang
# @File    : operation_ini.py
# @Software: PyCharm
import ConfigParser

config = ConfigParser.ConfigParser()
config.read(".\\tomorrow.ini")
print config.sections()
# print config.options('SectionOne')

cfgfile = open(".\\tomorrow.ini", 'w')

# add the settings to the structure of the file, and lets write it out...
config.add_section('Person')
print config.options('Person')
config.set('Person', 'HasEyes', True)
config.set('Person', 'Age', 50)
config.write(cfgfile)
cfgfile.close()
