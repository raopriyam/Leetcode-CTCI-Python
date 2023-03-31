# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 22:05:05 2023

@author: priya
"""

def tupleList(string):
    return string.split(","),tuple(string.split(","))


print(tupleList("1,2,3,4,5"))