# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:21:25 2021

@author: priya
"""

def strReverse1(s):
    s = "".join(reversed(s))
    return (s,reversed(s))
    #ans = swap(s)
    #return "".join(ans)

def strReverse2(s):
    ans = swap(s)
    return ("".join(ans),ans)

def strReverse3(s):
    return s[::-1]

def swap(s):
    s = list(s)
    left = 0
    right = len(s)-1
    while left < right:
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left += 1
        right -= 1
    return s
    
print(strReverse1("priyam"))
    
print(strReverse2("priyam"))

print(strReverse3("priyam"))

print(strReverse1(["p","r","i","y","a","m"]))

print(strReverse2(["p","r","i","y","a","m"]))

print(strReverse3(["p","r","i","y","a","m"]))