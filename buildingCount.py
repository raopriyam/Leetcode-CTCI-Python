# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 22:52:19 2023

@author: priya
"""

# Jack is walking down a street with n tall buildings lined up. 
# Calculate how many buildings he can see from each building. 
# (When the front building is taller than or equal to the back one, 
# the back one is blocked; Jack's current building can be seen by default)
# For example, input: [5,3,8,3,2,5]
# Output: [3,3,5,4,4,4]

def buildingCount(buildings = [5,3,8,3,2,5]):
    ans = []
    left = -1
    right = len(buildings)
    leftmax = 0
    rightmax = 0
    for i in range(len(buildings)):
        buildingCount = 1
        if i>0:
            left = i-1
            buildingCount += 1
            leftmax = buildings[left]
            left -= 1
        if i < len(buildings)-1:
            right = i+1 
            buildingCount += 1
            rightmax = buildings[right]
            right += 1
        while left>=0 or right<len(buildings):
            if left >= 0 and buildings[left] > leftmax:
                buildingCount += 1
                leftmax = buildings[left]
            left -= 1
            if right <= len(buildings)-1 and buildings[right] > rightmax:
                buildingCount += 1
                rightmax = buildings[right]
            right += 1
        ans.append(buildingCount)
    return ans
    
print(buildingCount([5,3,8,3,2,5]))
