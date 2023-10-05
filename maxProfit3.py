# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:56:35 2023

@author: priya
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = 0
        right = left +1
        ans = 0
        leng = len(prices)
        while right<leng:
            if prices[left] > prices[right]:
                left = right
            else:
                if prices[right] > prices[left]:
                    ans = ans + (prices[right] - prices[left])
                    left = right
            right += 1
        return ans