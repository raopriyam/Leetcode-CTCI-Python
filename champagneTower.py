# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:55:05 2023

@author: priya
"""

class Solution(object):
    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        dp = [[0.0 for _ in range(query_glass + 2)] for _ in range(query_row + 1)]
        dp[0][0] = poured

        for i in range(query_row):
            for j in range(query_glass+1):
                q = max(dp[i][j] - 1.0,0)/2
                dp[i+1][j] += q
                dp[i+1][j+1] += q

        return min(dp[query_row][query_glass],1.0)