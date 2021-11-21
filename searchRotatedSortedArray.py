# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 23:39:39 2021

@author: priya
"""

def searchRotatedSortedArray(arr,target):
    l , r = 0, len(arr)-1
    mid = 0
    
    while l<=r:
        mid= (l+r)//2
        if target == arr[mid]:
            return mid
        if arr[l] <= arr[mid]:
            if target>arr[mid] or target < arr[l]:
                l = mid+1
            else:
                r = mid-1
        else:
            if target<arr[mid] or target>arr[r]:
                r = mid-1
            else:
                l= mid + 1
                
    return -1

print(searchRotatedSortedArray([4,5,6,7,0,1,2],0))