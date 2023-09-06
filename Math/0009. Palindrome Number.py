# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 18:07:30 2023

@author: Seal-Rumi
"""

def isPalindrome(x):
    if (str(x)==str(x)[::-1]):
        return True
    else:
        return False
   
#Test
x = input()
print(isPalindrome(x))