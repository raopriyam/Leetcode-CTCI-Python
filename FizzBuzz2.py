# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 00:33:22 2025

@author: priya
"""

def FizzBuazz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)
            

FizzBuazz(15)