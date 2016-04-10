# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:11:25 2016

@author: KG
"""

class Card:
    """
    Heart = 0
    Spades = 1
    Clubs = 2    
    Diamonds 3
    """
    suite = -1
    value = -1
    
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def displayCard(self):
        print ("Suite :", self.suite,  "-- Value:", self.value)