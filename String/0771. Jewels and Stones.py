# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 23:37:56 2023

@author: Seal-Rumi
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        n = 0
        for i in jewels:
            n += stones.count(i)
        return n