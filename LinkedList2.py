# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 21:56:00 2022

@author: priya
"""

class LinkedListNode:
    def __init__(self,value,nextNode= None):
        self.value = value
        self.nextNode = nextNode
        
        
class LinkList:
    def __init__(self,head=None):
        self.head = head
        
    def insert(self, value):
        node = LinkedListNode(value)
        if self.head is None:
            self.head = node
            return 
        curr = self.head
        while True:
            if curr.nextNode is None:
                curr.nextNode = node
                break
            curr = curr.nextNode 
                
                
    def printLinkedList(self):
        curr =self.head
        while curr is not None:
            print(curr.value,"->",end=" ")
            curr = curr.nextNode 
        print(None)
lob1 = LinkList()
lob1.printLinkedList()
lob1.insert(1)
lob1.printLinkedList()
lob1.insert(2)
lob1.printLinkedList()
lob1.insert(3)
lob1.printLinkedList()



        
            
            
        