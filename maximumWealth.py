# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:46:37 2023

@author: priya
"""

def maximumWealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    numOfCustomers = len(accounts)
    numOfAccounts = len(accounts[0])
    ans = [0]*numOfCustomers
    for i in range(numOfCustomers):
        for j in range(numOfAccounts):
            ans[i] = ans[i] + accounts[i][j]
    return max(ans)

print(maximumWealth( [[1,2,3],[1,3,2]]))