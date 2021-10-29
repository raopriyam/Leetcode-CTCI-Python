# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 16:03:56 2021

@author: priya
"""

def frequency(s):
    slen = len(s)
    ans = [0]*26
    i = 0
    while i<slen:
        value = 0
        if i+2>slen or s[i+2] != "#":
            value = ord(s[i]) - ord("0")
            ans[value-1] += 1
            i += 1
        elif s[i+2] == "#":
            value = (ord(s[i]) -ord("0"))*10 + (ord(s[i+1])-ord("0"))
            ans[value-1] += 1
            i += 3
        if i<slen:
            if s[i] == "(":
                j = i+1
                while s[j] != ')':
                    j = j+1
                frequent = int(s[i+1:j])
                print()
                ans[value-1] += frequent - 1
                i = j+1
    return ans

print(frequency("1226#24#"))
print(frequency("1(2)23(3)"))
print(frequency("2110#(2)"))
print(frequency("23#(2)24#25#26#23#(3)"))