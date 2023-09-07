# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:55:47 2023

@author: Seal-Rumi
"""

class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        return n+n*(n%2==1)