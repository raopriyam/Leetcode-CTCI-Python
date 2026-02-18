# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:32:02 2026

@author: priya
"""

def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    left = 0
    right = 1
    profit = 0
    lenPrices = len(prices)

    while right < lenPrices:
        if prices[left] < prices[right]:
            currProfit = prices[right] - prices[left]
            profit = max(profit,currProfit)
        else:
            left = right
        right += 1

    return profit

    