# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 18:32:00 2021

@author: priya
"""

def intToRoman( num):
        """
        :type num: int
        :rtype: str
        """
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = ""
        while num>0:
            if num >= dic["M"]:
                num = num-dic["M"]
                ans = ans + "M"
            elif num == 900:
                num = num-900
                ans = ans + "CM"
            
            elif num >= dic["D"]:
                num = num-dic["D"]
                ans = ans + "D"
            elif num == 400:
                num = num-400
                ans = ans + "CD"
            elif num >= dic["C"]:
                num = num-dic["C"]
                ans = ans + "C"
            elif num == 90:
                num = num-90
                ans = ans + "XC"
            elif num >= dic["L"]:
                num = num-dic["L"]
                ans = ans + "L"
            elif num == 40:
                num = num-40
                ans = ans + "XL"
            elif num >= dic["X"]:
                num = num-dic["X"]
                ans = ans + "X"
            elif num == 9:
                num = num-9
                ans = ans + "IX"
            elif num >= dic["V"]:
                num = num-dic["V"]
                ans = ans + "V"
            elif num == 4:
                num = num-4
                ans = ans + "IV"
            elif num >= dic["I"]:
                num = num-dic["I"]
                ans = ans + "I"
            
        return ans
    
print(intToRoman(123))