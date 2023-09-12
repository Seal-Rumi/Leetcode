# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:43:30 2023

@author: Seal-Rumi
"""

class Solution:
    def numberOfMatches(self, n: int) -> int:
        output = 0
        teams = n
        while teams != 1:
            if teams%2:
                output += (teams-1)//2
                teams = (teams-1)//2 +1
            else:
                output += teams//2
                teams //= 2
        return output