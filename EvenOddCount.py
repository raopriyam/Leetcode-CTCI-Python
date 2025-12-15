# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:40:19 2025

@author: priya
"""

def EvenOddCount(list1):
    EvenCount = 0
    OddCount = 0
    
    for i in list1:
        if i%2 == 0:
            EvenCount += 1
        else:
            OddCount += 1
            
    return "Even count is" , EvenCount, "/n Odd count is ", OddCount 


print(EvenOddCount([1,2,3,4,5,6,7,8,9,11]))