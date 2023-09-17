# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 22:34:54 2023

@author: priya
"""

class Solution:
    def calculate(self,s):
        num = 0
        op = "+"
        
        stack = []
        
        def helper(op,num):
            if op == "+":
                stack.append(num)
            elif op == "-":
                stack.append(-num)
            elif op == "*":
                stack.append(stack.pop() * num)
            elif op == "/":
                stack.append(stack.pop() / num)
                
        for i in range(len(s)):
            if s[i].isdigit():
                num = num*10 + int(s[i])
            elif s[i] == '(':
                stack.append(op)
                num = 0
                op = "+"
            elif s[i] in ["+","-","*","/",")"]:
                helper(op,num)
                if s[i] == ")":
                    num = 0
                    while isinstance(stack[-1], int):
                        num += stack.pop()
                    op = stack.pop()
                    helper(op,num)
                num = 0
                op = s[i]
                
        helper(op,num)
        
        return sum(stack)
                
                
                
                
                
                
                
                