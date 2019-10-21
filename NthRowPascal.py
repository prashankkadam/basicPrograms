# -*- coding:/ utf-8 -*-
"""
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
Email ID : prashank.kadam@maersktankers.com
Created on - Tue Oct 21 2019
version : 1.0
"""

# Returning the nth row in a pascals triangle


def pascal_line(n):
    line = [1]
    mid, even = divmod(n, 2)
    for k in range(1, mid + 1):
        num = int(line[k - 1] * (n + 1 - k) / (k))
        line.append(num)
    reverse_it = reversed(line)
    if not even:
        next(reverse_it)
    for n in reverse_it:
        line.append(n)
    return line


i = int(input())
print(pascal_line(i - 1))
