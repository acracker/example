#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-07 9:43
# @Author  : pang
# @File    : 2.py
# @Software: PyCharm
import random

import numpy as np
import pandas as pd
import threading
import time
lock = threading.RLock()

index = list("ABCDEF")
columns = list("abcdef")

df = pd.DataFrame(np.random.randn(6, 6), index=index, columns=columns)


def store(_df):
    _df.to_csv("xx.csv", encoding='utf-8')


def foo():

    for x in range(10):

        # time.sleep(100)
        for i in range(10):
            dct = {}
            for j in range(3):
                _index = random.choice(index)
                _column = random.choice(columns)
                _value = random.randint(0, 1000)
                dct[(_index, _column)] = _value
                df.at[_index, _column] = _value
            # store(df)
            for _index, _column in dct.keys():
                if dct[(_index, _column)] != df.loc[_index][_column]:
                    print "dict value: %s, df value: %s" % (dct[(_index, _column)], df.loc[_index][_column])
        dct = dict()
        for _k in columns:
            dct[_k] = random.randint(1, 200)
        _index = random.choice(columns) + random.choice(columns) + str(random.randint(0, 1000))
        df.loc[_index] = dct
        index.append(_index)

        # for _column in dct.keys():
        #     if dct[_column] != df.loc[_index][_column]:
        #         print "2, !=", dct[_column], df.loc[_index][_column]
        lock.acquire()
        time.sleep(100)
        store(df)
        lock.release()

threads = []
threads.append(threading.Thread(target=foo))
# threads.append(threading.Thread(target=foo))
# threads.append(threading.Thread(target=foo))
# threads.append(threading.Thread(target=foo))
# threads.append(threading.Thread(target=foo))
# threads.append(threading.Thread(target=foo))
# threads.append(threading.Thread(target=foo))
for t in threads:
    t.setDaemon(True)
    t.start()

