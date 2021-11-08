# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 21:44:21 2021

@author: priya
"""

def countSegmentsOfString(s):
    if s == "":
        return 0
    s = s.split(" ")
    count = 0
    for i in s:
        if i != '':
            count += 1
    return count


print(countSegmentsOfString("my name is priyam rao"))