# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 22:29:00 2023

@author: priya
"""

def fizzBuzz(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []
    for i in range(1,n+1):
        if (i % 3 == 0) and (i%5 == 0):
            ans.append("FizzBuzz")
        elif (i % 3 == 0) and (i%5 != 0):
            ans.append("Fizz")
        elif (i % 3 != 0) and (i%5 == 0):
            ans.append("Buzz")
        else:
            ans.append(str(i))
    return ans

print(fizzBuzz(10))