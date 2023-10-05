# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:46:31 2023

@author: priya
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ans = 0
        left = 0
        right = left+1
        leng = len(prices)
        while right < leng:
            if prices[left] > prices[right]:
                left = right
            else:
                if prices[right] - prices[left] > ans:
                    ans = prices[right] - prices[left]
            right += 1 
        return ans