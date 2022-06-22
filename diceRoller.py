# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:44:03 2022

@author: priya
"""

import random

def inputCheck(i):
    if i == 1:
        print("\nthe number on dice is: ",random.randrange(1,6,1))
    elif i == 0:
        return "Program ended"
    else:
        print("wrong input")
    

def diceRoller():
    inp = int(input("enter your choice \n 1 to roll dice \n 0 to Quit \n"))
    while inp !=0:
         inputCheck(inp)
         inp = int(input("enter your choice \n 1 to roll dice \n 0 to Quit \n"))
        
diceRoller()