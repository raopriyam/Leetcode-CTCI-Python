# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 23:28:07 2021

@author: priya
"""

def isNameThere(names,name):
    for i in names:
        if name == i:
            return True
    return False
    
print(isNameThere(["priyam","Rao","K"],"Raop"))