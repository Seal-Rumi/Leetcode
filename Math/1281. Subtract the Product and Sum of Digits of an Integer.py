# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 21:08:13 2023

@author: Seal-Rumi
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        num = [int(i) for i in num]
        Product = 1
        Sum = sum(num)
        for i in num:
            Product *= i
        return Product - Sum