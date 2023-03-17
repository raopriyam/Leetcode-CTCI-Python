# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:55:59 2023

@author: priya
"""

def palindromePermutationString2(string):
    string = string.replace(" ","")
    string = string.lower()
    
    check = {}
    chk = 0
    
    for i in string:
        if i in check:
            check[i] = check[i] -1
        else:
            check[i] = 1
            
    for i in check:
        if check[i] == 1:
            chk = chk + 1
    
    if chk == 1:
        return True
    
    return False

print(palindromePermutationString2("priYamy arip"))