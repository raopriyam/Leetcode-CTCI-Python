# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 20:58:48 2023

@author: priya
"""

def isUnique3(string):
    checkString = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i in checkString:
            checkString.replace(i,"")
        else:
            return False
    return True

print(isUnique3("priyam Rao"))