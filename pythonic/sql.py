#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-06-22 14:06
# @Author  : pang
# @File    : sql.py
# @Software: PyCharm

# mysql 插入数据遇到 主键或者唯一key 重复,则更新数据. DUPLICATE KEY UPDATE

import six
item = {'name': 'NAME', 'age': "AGE", 'sex': "SEX", "table_name": "table_name"}
table_name = item.pop('table_name')
col_str = ''
row_str = ''
for key in item.keys():
    col_str = col_str + " " + key + ","
    row_str = "{}'{}',".format(row_str, item[key] if "'" not in item[key] else item[key].replace("'", "\\'"))
    sql = "insert INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE ".format(table_name, col_str[1:-1], row_str[:-1])

print(sql)
for (key, value) in six.iteritems(item):
    sql += "{} = '{}', ".format(key, value if "'" not in value else value.replace("'", "\\'"))
sql = sql[:-2]
print(sql)

# sql .多条记录
"""
INSERT INTO clients  
(client_id,client_name,client_type)  
SELECT supplier_id,supplier_name,'advertising'  
FROM suppliers  
WHERE not exists(select * from clients where clients.client_id=suppliers.supplier_id);  
"""


# 插入单条记录 使用 dual 做表名可以让你在 select 语句后面直接跟上要插入字段的值，即使这些值还不存在当前表中。
"""
INSERT INTO clients  
(client_id,client_name,client_type)  
SELECT 10345,'IBM','advertising'  
FROM dual  
WHERE not exists (select * from clients where clients.client_id=10345);  

"""


# 方法三:
"""
REPLACE INTO users(id, name, age)
"""
