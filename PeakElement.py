# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 20:43:52 2021

@author: priya
"""

def peakElement(arr, n):
    if len(arr) == 0:
        return 0
    elif len(arr) == 1:
        return 1
    elif len(arr) == 2:
        if arr[0] == arr[1]:
            return 0
        else:
            return 1
    else:
        count = 0
        if arr[0]>arr[1]:
            count = count + 1
        
        for i in range(1,len(arr)-1):
            if i == len(arr)-2:
                if arr[i+1]>arr[i]:
                    count = count+1
                    continue
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                count = count + 1
    return count


print(peakElement([7,1,5,3,4],4))