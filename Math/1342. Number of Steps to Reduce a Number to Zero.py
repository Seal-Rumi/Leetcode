# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:47:27 2023

@author: Seal-Rumi
"""

class Solution:
    def numberOfSteps(self, num: int) -> int:
        step = 0
        n = num
        while n!=0:
            if n%2:
                n-=1
            else:
                n//=2
            step +=1
        return step