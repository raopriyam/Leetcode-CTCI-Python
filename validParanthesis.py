# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 12:01:40 2026

@author: priya
"""

def isValid(self, s: str) -> bool:
    dictionary = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }
    set1 = {'(','{','['}
    stack = [] 
    for i in s:
        if i in set1:
            stack.append(i)
        else:
            if stack == []:
                return False
            elif i != dictionary[stack[-1]] :
                return False
            stack.pop()
    return len(stack) == 0
