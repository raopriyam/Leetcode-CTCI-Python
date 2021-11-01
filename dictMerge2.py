# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 23:32:34 2021

@author: priya
"""

def dictMerge2(dict1,dict2):
    return {**dict1,**dict2}

print(dictMerge2({"1":1,"2":2},{"3":3,"4":4}))