# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 21:24:15 2021

@author: priya
"""

def removeElementFormList1(arr):
    arr = list(set(arr))
    return arr 

print(removeElementFormList1([0,1,1,2,3,3,4,5,5,5,6]))