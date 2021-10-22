# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 02:41:39 2021

@author: priya
"""

#check1 , check2 = [1, 5, 7, 1],[1, 1, 1, 1]



def checkSumPair(arr,sum1):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            if i!=j and arr[i]+arr[j] == sum1:
                count += 1
    return count


print(checkSumPair([1, 2, 3, 1],3))

print(checkSumPair([1, 5, 7, 1],2))