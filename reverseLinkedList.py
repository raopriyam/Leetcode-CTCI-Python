# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 14:20:15 2021

@author: priya
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        h = self.head
        while h:
            print(h.val)
            h = h.next
    
    def reverseLinkedList(self,head):
        prev , curr = None ,  head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr 
            curr = next_node
        return prev
    
list1 = LinkedList()
list1.head = Node(1)
e2 = Node(2)
list1.head.next = e2
e3 = Node(3)
e2.next = e3
e4 = Node(4)
e3.next = e4
e5 = Node(5)
e4.next = e5
e6 = Node(6)
e5.next = e6
e7 = Node(7)
e6.next = e7
e8 = Node(8)
e7.next = e8
e9 = Node(9)
e8.next = e9
e10 = Node(10)
e9.next = e10

list1.printList()
list1.head = list1.reverseLinkedList(list1.head)

list1.printList()