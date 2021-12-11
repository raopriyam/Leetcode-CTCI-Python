# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 13:31:51 2021

@author: priya
"""

def printDictWithList(dict1):
    ls1 = []
    ls2 = []
    for i in dict1:
        ls1.append(i)
        ls2.append(dict1[i])
    for k in range(len(ls1)):
        print(ls1[k]," : ",ls2[k])
        
printDictWithList({"a":1,"b":2,"c":3})