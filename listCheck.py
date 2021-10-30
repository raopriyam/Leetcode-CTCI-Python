# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 22:15:41 2021

@author: priya
"""

def listCheck(list1):
    for i in list1:
        if i >= 0:
            pass
        else:
            return False
    return True

print(listCheck([1,2,3,4,5,6]))
print(listCheck([1,2,'a',4,5,6]))
print(listCheck([1,2,'c',4,5,6]))