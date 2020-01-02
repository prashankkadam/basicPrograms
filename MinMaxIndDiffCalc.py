# -*- coding:/ utf-8 -*-
"""
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
Email ID : prashank.kadam@maersktankers.com
Created on - Tue Oct 21 2019
version : 1.0
"""

# Code to calculate the difference in the maximum and minimum indices of
# all the elements in the list and return the maximum diffence

# Importing the required libraries 
import ast
import numpy as np

# Taking input list from the user
input_list = ast.literal_eval(input())
unique_list = np.unique(input_list)
final = []

# Enumerating and finding the differences
for i in unique_list:
    indices = [m for m, x in enumerate(input_list) if x == i]
    diff = np.max(indices) - np.min(indices)
    final.append(diff)

print(np.max(final))
