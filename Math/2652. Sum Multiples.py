# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:37:05 2023

@author: Seal-Rumi
"""

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        res = 0
        for i in range(1, n+1):
            if not (i%3)or not(i%5)or not (i%7):
                res += i
        return res