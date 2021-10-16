# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 22:27:22 2021

@author: priya
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None        
        
    def convertNumber(self):
        sum1 = 0
        current = self.head
        while current != None:
            sum1 = sum1*10 + current.val
            current = current.next
        return sum1

list1 = LinkedList()
list1.head = Node(1)
e2 = Node(2)
list1.head.next = e2
e3 = Node(3)
e2.next = e3
num1 = list1.convertNumber()

list2 = LinkedList()
list2.head = Node(2)
l2 = Node(5)
list2.head.next = l2
l3 = Node(3)
l2.next = l3
num2 = list2.convertNumber()

print(num1)
print(num2)
print()
print(num1 + num2)