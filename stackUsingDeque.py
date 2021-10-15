# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 22:26:18 2021

@author: priya
"""

from collections import deque
myStack = deque()

myStack.append(1)
myStack.append(2)
myStack.append(3)
myStack.append(4)
myStack.append(5)

def stackPop():
    if myStack:
        myStack.pop()
        print()
    else:
        print("stackempty")

print(myStack)

stackPop()
print(myStack)

stackPop()
print(myStack)

stackPop()
print(myStack)

stackPop()
print(myStack)

stackPop()
print(myStack)

stackPop()
print(myStack)
