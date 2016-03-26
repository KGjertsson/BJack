# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:11:25 2016

@author: KG
"""

class Card:
    suite = -1
    value = -1
    
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        
    def displayCard(self):
        print "Suite : ", self.suite,  ", Value: ", self.Value