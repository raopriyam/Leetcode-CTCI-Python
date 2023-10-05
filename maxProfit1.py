# -*- coding: utf-8 -*-
"""
Created on Wed Oct  4 19:30:03 2023

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
        leng = len(prices)-1
        while left<leng:
            maxProfit = max(prices[left+1:])
            if maxProfit - prices[left] > ans:
                ans = maxProfit - prices[left]
            left += 1
        return ans
    
ob1 = Solution()
output = ob1.maxProfit([7,1,3,5,4])
assert output == 4
print(output)