# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 23:17:42 2021

@author: priya
"""

def pattern2(n):
    for i in range(n+1):
        for j in range(i):
            print(i,end ="")
        print()

pattern2(5)
            