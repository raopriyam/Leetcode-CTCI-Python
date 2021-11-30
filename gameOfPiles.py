# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 23:30:40 2021

@author: priya
"""


def gameOfPiles(piles, k):
    # Write your code here
    check = 0
    for i in range(len(piles)):
        temp = piles[i]//k
        piles[i] = piles[i] - (temp*k)
        check = check+temp
    check = check + sum(piles)
    if check%2 == 0:
        return "Alex wins the game of $len(piles) pile(s)"
    else:
        return "Sam wins the game of $len(piles) pile(s)"
    
print(gameOfPiles([3,6,7],1))