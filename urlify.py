# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 13:18:01 2021

@author: priya
"""

def urlify(s):
    s =s.replace(" ","%30")
    return s

print(urlify("Priyam Rao Is my name"))

print()
print()
def urlify2(s):
    ans = ""
    for i in s:
        if i==" ":
            ans = ans + "%20"
        else:
            ans = ans + i
    return ans
        

print(urlify2("Priyam Rao Is my name"))