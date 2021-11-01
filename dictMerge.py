# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:30:12 2021

@author: priya
"""

def dictMerge(dict1,dict2):
    dict3 = dict1
    dict3.update(dict2)
    return dict3 


print(dictMerge({"1":1,"2":2},{"3":3,"4":4}))