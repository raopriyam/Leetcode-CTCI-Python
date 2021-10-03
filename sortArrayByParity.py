# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:14:31 2021

@author: priya
"""

def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = []
        odd = []
        res = []
        for i in range(len(nums)):
            if nums[i]%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        #print(even)
        #print(odd)
        res.extend(even)
        res.extend(odd)
        return res
        
        # ind = 0
        # for i in range(len(nums)):
        #     if nums[i]%2 == 0:
        #         temp = nums[ind]
        #         nums[ind] = nums[i]
        #         ind = ind + 1
        #         nums[i] = temp
        # return nums