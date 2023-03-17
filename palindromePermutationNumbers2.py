# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 22:13:15 2023

@author: priya
"""

def palindromePermutationNumber2(n):
    string = str(n)

    check = {}
    chk = 0
    
    for i in string:
        if i in check:
            check[i] = check[i] + 1
        else:
            check[i] = 1

    for i in check:
        if check[i] % 2 != 0:
            chk = chk + 1
            
    return chk == 1

print(palindromePermutationNumber2(123423144))