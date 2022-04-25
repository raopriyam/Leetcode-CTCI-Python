# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 22:08:47 2022

@author: priya
"""

def SortWords(s):
    final = []
    s1 = s.split()
    for i in s1:
        final.insert(ord(i[-1]),i[:-1])
        print(int(i[-1]))
    print(final)
    return " ".join(final)

print(SortWords("is3 my1 Priyam4 name2"))
        
        
        
    