# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 23:03:01 2021

@author: priya
"""

list1 = [1,2,3,4,5,6,7,8,9]
left = 0
right = len(list1)-1
mid = 0
target = 7
while left<right:
    mid = int((right+left)/2-1)
    if target <list1[mid]:
        right = mid
    elif target>list1[mid]:
        left = mid
    else:
        print(mid)
    
    