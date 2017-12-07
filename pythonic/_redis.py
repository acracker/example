#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-22 17:55
# @Author  : pang
# @File    : _redis.py
# @Software: PyCharm

import redis
import time
import json

# redis_pool = redis.ConnectionPool(host='120.27.196.231', port=1234, password='uxmc2017.')
# r = redis.StrictRedis(connection_pool=redis_pool)
# client = redis.Redis(host='120.27.196.231', port=1234, password='uxmc2017.')


redis_pool = redis.ConnectionPool(host='120.27.196.231', port=1234, password='uxmc2017.')
client = redis.StrictRedis(connection_pool=redis_pool)

key_name = "simuwang:CompanyItem"
index = 0
while True:
    # print client.brpoplpush(key_name, key_name + ":backup")
    json_data = client.brpoplpush(key_name, key_name)
    json_data = json.loads(json_data)
    company_id = json_data['company_id']
    data = json.loads(json_data['json_data'])
    corestrategy = data['corestrategy']
    print corestrategy, company_id
    if index > 20:
        break
    index += 1
