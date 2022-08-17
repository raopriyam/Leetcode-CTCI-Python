# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 22:59:30 2022

@author: priya
"""

def palindromePermutation(s):
    list1 = [0]*26
    for i in s:
        a = ord(i)-97
        if list1[a] == 0:
            list1[a] = 1
        elif list1[a] == 1:
            list1[a] = 0
    if sum(list1) > 1:
        return False
    return True
    
print(palindromePermutation("abcabd"))