# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 17:50:40 2021

@author: priya
"""

class ListNode:
   def __init__(self, data, next = None):
      self.data = data
      self.next = next
class Solution(object):
   def getIntersectionNode(self, headA, headB):
      """
      :type head1, head1: ListNode
      :rtype: ListNode
      """
      dict = {}
      while headA:
         dict[headA]=1
         headA = headA.next
      while headB:
         if headB in dict:
            return headB
         headB = headB.next
      return None
headA = ListNode(4)
headB = ListNode(5)
Intersect = ListNode(8, ListNode(4, ListNode(5)))
headA.next = ListNode(1, Intersect)
headB.next = ListNode(2, ListNode(6, ListNode(7)) )
ob1 = Solution()
op = ob1.getIntersectionNode(headA, headB)
if op:
    
    print("Intersection:",op.data)
    
else:
    print("no intersection")
