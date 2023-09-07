# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:50:11 2023

@author: Seal-Rumi
"""

class Solution:
    def countDigits(self, num: int) -> int:
        n = [int(i) for i in str(num)]
        res = 0
        for i in n:
            if not num%i:
                res += 1
        return res