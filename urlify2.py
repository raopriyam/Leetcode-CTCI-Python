# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 18:39:29 2022

@author: priya
"""

def urlify(s):
    s = s.replace(" ","%20")
    return s

print(urlify("priyam rao"))