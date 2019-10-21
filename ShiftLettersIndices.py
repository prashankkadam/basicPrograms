# -*- coding:/ utf-8 -*-
"""
This piece of software is bound by The MIT License (MIT)
Copyright (c) 2019 Prashank Kadam
Code written by : Prashank Kadam
Email ID : prashank.kadam@maersktankers.com
Created on - Tue Oct 21 2019
version : 1.0
"""

# Shift letters in a word by a certian index to make a new word (basic encryption)

alphabets = 'abcdefghijklmnopqrstuvwxyz'
alphabets_caps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lst = []

word = input()
word = word.replace('[', '')
word = word.replace(']', '')
lst = word.split()

new_word = ""
for letter in lst[0]:
    if letter in alphabets:
        index_val = alphabets.index(letter) - (int(lst[1]) % 26)
        new_word += alphabets[index_val]
    elif letter in alphabets_caps:
        index_val = alphabets_caps.index(letter) - (int(lst[1]) % 26)
        new_word += alphabets_caps[index_val]

print(new_word)