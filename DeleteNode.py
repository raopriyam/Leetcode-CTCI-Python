# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 23:34:09 2021

@author: priya
"""

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        