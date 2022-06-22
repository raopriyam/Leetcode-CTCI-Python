# -*- coding: utf-8 -*-
"""
Created on Sat Apr 30 23:33:55 2022

@author: priya
"""

def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    count = 0
    for i in accounts:
        if sum(i)>count:
            count = sum(i)
        
    return count


print(maximumWealth([[1,2,3],[3,2,1]]))