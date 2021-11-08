# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:41:58 2021

@author: priya
"""

def reverseVowels(s):
    s = list(s)
    left = 0
    right = len(s)-1
    set1 = {"a","A","e","E","i","I","o","O","u","U"}
    while left<right:
        while s[left] not in set1 and left < right:
            left += 1
        while s[right] not in set1 and right > left:
            right -= 1
        temp = s[left]
        s[left] = s[right]
        s[right] = temp
        left = left +1
        right = right -1
    return "".join(s)


print(reverseVowels("priyam"))
print(reverseVowels("hello"))
print(reverseVowels("suyog"))
print(reverseVowels("spaghetti"))
print(reverseVowels("pisutttek"))

            
        