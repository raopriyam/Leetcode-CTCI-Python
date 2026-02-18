# -*- coding: utf-8 -*-
"""
Created on Tue Feb 17 21:33:45 2026

@author: priya
"""

def slowestKey(self, releaseTimes, keysPressed):
    """
    :type releaseTimes: List[int]
    :type keysPressed: str
    :rtype: str
    """
    ans = [0]*26
    ans[ord(keysPressed[0])-97] = releaseTimes[0]
    for i in range(1,len(releaseTimes)):
        tempVal = releaseTimes[i] - releaseTimes[i-1]
        ans[ord(keysPressed[i])-97]  = max(tempVal,ans[ord(keysPressed[i])-97] )

    maxValue = max(ans)
    for j in range(25,-1,-1):
        if ans[j] == maxValue:
            return chr(j+97)


