# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 13:33:53 2023

@author: Seal-Rumi
"""
#Brute Force
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for l in range(1, n + 1, 2):
            for i in range(n - l + 1):
                res += sum(arr[i:i + l])
        return res
    
