# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:11:25 2016
"""

class Card:
    """
    Heart = 0
    Spades = 1
    Clubs = 2    
    Diamonds 3
    """
    
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value

    def displayCard(self):
        if self.value == 11:
            name = "Jack"
        elif self.value == 12:
            name = "Queen"
        elif self.value == 13:
            name = "King"
        elif self.value == 1:
            name = "Ace"
        else:
            name = self.value
            
        if self.suite == 0:
            tail = "of hearts"
        elif self.suite == 1:
            tail = "of spades"
        elif self.suite == 2:
            tail = "of clubs"
        else:
            tail = "of diamonds"

        print(name, tail)
