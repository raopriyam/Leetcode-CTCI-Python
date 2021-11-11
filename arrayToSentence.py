# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 23:12:05 2021

@author: priya
"""

def arrayToSentence(arr):
    sentence = ""
    for i in arr:
        sentence = sentence  + str(i) + " "
    return sentence
        
print(arrayToSentence(["my","name","is","priyam","rao"]))