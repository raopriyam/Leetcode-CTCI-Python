# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 22:25:21 2023

@author: priya
"""

import itertools, random

deck = list(itertools.product(range(1,14),['SPADE','HEART','DIAMOND','CLUB']))
random.shuffle(deck) 
print("Your Cards are:")
for i in range(5):
    print(deck[i][0], "of", deck[i][1])                                                                 