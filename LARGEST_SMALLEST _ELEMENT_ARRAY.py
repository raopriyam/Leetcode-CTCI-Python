# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 20:55:02 2021

@author: priya
"""

def largest_smallest(nums):
    min1 = nums[0]
    max1 = nums[0]
    for i in nums:
        if i<min1:
            min1 = i
        elif i>max1:
            max1 = i
    print("minimum =",min1)
    print("maximum =",max1)
    
#largest_smallest([2,4,7,-6,5,1,3])



def lar_small(nums):
    nums.sort()
    print("minimum =",nums[0])
    print("maximum =",nums[-1])
    
#lar_small([2,4,7,-6,5,1,3])



def lar_small1(nums):
    print("minimum =",min(nums))
    print("maximum =",max(nums))
    
lar_small1([2,4,7,-6,5,1,3])
    

            
            
    