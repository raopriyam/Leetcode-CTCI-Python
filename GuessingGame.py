# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 23:02:38 2025

@author: priya
"""

import random

number = random.randint(1, 50)

while True:
    guess = int(input("Guess a number between 1 and 50: "))
    
    if guess == number:
        print("Correct! You win!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
