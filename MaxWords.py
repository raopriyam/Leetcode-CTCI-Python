# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 21:58:25 2022

@author: priya
"""

def maxWords(sentences):
    maxVal = 0
    for i in sentences:
        check1 = i.split(" ")
        if maxVal <= len(check1):
            maxVal = len(check1)
            
    return maxVal 

print(maxWords(["i am Priyam","My name is priyam Rao","What is the name of your country?"]))