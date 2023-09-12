# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:08:47 2023

@author: Seal-Rumi
"""

class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:return n
        Fib = [0, 1]
        for i in range(2, n+1):
            Fib.append(Fib[i-2]+Fib[i-1])
        return Fib[-1]