# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:59:21 2023

@author: Seal-Rumi
"""

class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0])-97
        y = int(coordinates[1])
        return (x+y)%2==0