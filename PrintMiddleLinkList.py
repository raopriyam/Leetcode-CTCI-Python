# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 22:10:41 2021

@author: priya
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        
        
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        
    def printList(self):
        current = self.head
        while current.next:
            print(current.val)
        
    def printMiddle(self):
        middle = self.head
        last = self.head
        while last.next:
            middle = middle.next
            if last.next.next:
                last = last.next.next
            else:
                break
        print(middle.val)
        
LinkList1 = LinkedList()
LinkList1.push(1)
LinkList1.push(2)
#LinkList1.push(3)
#LinkList1.push(4)
#LinkList1.push(5)
LinkList1.printMiddle()

