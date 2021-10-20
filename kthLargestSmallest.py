# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 02:50:00 2021

@author: priya
"""

def kthLargestSmallest(arr,k):
    arr.sort()
    kthSmall = arr[k-1]
    kthLarge = arr[len(arr)-k]
    return kthSmall,kthLarge


print(kthLargestSmallest([9,1,3,5,4,2,6,8,7,10],4))