# -*- coding:/ utf-8 -*-
"""
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
Email ID : prashank.kadam@maersktankers.com
Created on - Tue Oct 21 2019
version : 1.0
"""

# Code to flatten a nested dictionary

import ast, sys
from collections import MutableMapping as mm

input_str = sys.stdin.read()
input_dict = dict(ast.literal_eval(input_str))


def flatten_dict(d, parent_key='', sep='_'):
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, mm):
            items.extend(flatten_dict(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)


out1 = list(flatten_dict(input_dict).keys())
out2 = list(flatten_dict(input_dict).values())
out1.sort()
out2.sort()
print(out1)
print(out2)
