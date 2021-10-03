# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:13:26 2021

@author: priya
"""

def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        res = head.val
        while head.next != None:
            res = res*2 + head.next.val
            head = head.next
        return res