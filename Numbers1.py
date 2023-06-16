# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 16:06:25 2023

@author: priya
"""

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)