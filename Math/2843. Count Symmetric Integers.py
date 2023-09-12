# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:01:13 2023

@author: Seal-Rumi
"""


class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        symmetric = []
        for i in range(low, high+1):
            curr = [int(j) for j in str(i)]
            if len(curr)%2:continue
            if sum(curr[:len(curr)//2])==sum(curr[len(curr)//2:]):
                symmetric.append(i)
        return len(symmetric)