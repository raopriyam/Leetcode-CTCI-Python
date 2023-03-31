# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 22:14:24 2023

@author: priya
"""

def compute2(n):
    return n + int(str(n)+str(n)) + int(str(n)+str(n)+str(n))

print(compute2(5))