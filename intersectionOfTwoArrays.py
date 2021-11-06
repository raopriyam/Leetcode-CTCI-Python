# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:23:07 2021

@author: priya
"""

def intersection(nums1,nums2):
    dict1 = {}
    ans = []
    for i in nums1:
        if i not in dict1:
            dict1[i] = 0
        else:
            pass
                    
    for i in nums2:
        if i in dict1:
            ans.append(i)
    ans=list(set(ans))
    return ans


print(intersection([1,2,2,1],
[2,2]
))
    