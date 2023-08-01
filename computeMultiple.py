# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:05:10 2023

@author: priya
"""

a = int(input("Input an integer : "))
n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
print (n1+n2+n3)