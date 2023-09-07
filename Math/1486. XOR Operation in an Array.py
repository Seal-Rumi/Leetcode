# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:34:14 2023

@author: Seal-Rumi
"""

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start +2*i for i in range(1,n)]
        res = start
        for i in nums:
            res^=i
        return res