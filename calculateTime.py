# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 22:46:00 2023

@author: priya
"""

def calculateTime( keyboard, word):
    """
    :type keyboard: str
    :type word: str
    :rtype: int
    """
    sum1 = 0
    leng = len(word)
    for i in range(leng):
        if i == 0:
            sum1 = sum1 + ord(word[i]) - 96
        else:
            sum1 = sum1 + abs(ord(word[i]) - ord(word[i-1])) 
    return sum1

print(calculateTime("abcdefghijklmnopqrstuvwxyz", "cba"))