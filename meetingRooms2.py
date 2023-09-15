# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:04:17 2023

@author: priya
"""

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        ans = [0]
        intervals.sort()
        for time in intervals:
            if min(ans) > time[0]:
                ans.append(time[1])
            else: 
                ans[ans.index(min(ans))] = time[1]
        return len(ans)
