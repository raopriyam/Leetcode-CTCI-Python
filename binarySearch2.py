# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:46:50 2021

@author: priya
"""

def binarySearch(arr,target):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = l + (r-l)//2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            r = mid-1
        else:
            l = mid+1
    return -1

print(binarySearch([0,1,2,3,4,5,6,7,8],6))
          