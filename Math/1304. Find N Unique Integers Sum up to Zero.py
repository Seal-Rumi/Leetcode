# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 22:53:06 2023

@author: Seal-Rumi
"""

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2:
            return [(i//2 + 1)*(-1)**i for i in range(n-1)] + [0]
        else:
            return [(i//2 + 1)*(-1)**i for i in range(n)]