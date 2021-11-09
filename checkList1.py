# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 23:50:12 2021

@author: priya
"""

def checkList(list1):
    for i in list1:
        if i<=0:
            print(i)
            
            
print(checkList([1,2,-3,4,5]))