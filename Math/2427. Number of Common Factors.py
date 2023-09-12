# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 17:39:57 2023

@author: Seal-Rumi
"""

class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        output = 0
        for i in range(1,min({a,b})+1):
            if (not a%i) and (not b%i):
                output+=1
        return output