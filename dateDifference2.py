# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 23:07:49 2023

@author: priya
"""

from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)