# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 22:34:29 2023

@author: priya
"""

def fizzBuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
            
fizzBuzz()