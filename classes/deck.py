# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:57:42 2016
"""

from .card import Card
from random import *

class Deck():
    
    n_cards = 0
    cards = []
    
#    def __init__(self, n_decks):
#        suite = 1;
#        value = 1;
#        i=1;
#        n=1;
#        self.n_cards=52*n_decks
#        while n <= n_decks:
#            while suite <= 4:
#                while value <= 13:
#                    self.cards[i]=Card(suite,value)
#                    value=value+1
#                    i=i+1
#                suite=suite+1
#            n=n+1
    
    def __init__(self, n_decks):
        self.n_cards = 52 * n_decks
        n = 0
        while n < n_decks:
            suite = 0
            while suite < 4:
                value = 1
                while value <= 13:
                    self.cards.append(Card(suite,value))
                    value = value + 1
                suite = suite + 1
            n = n + 1
            
    def pullCard(self):
#        i=randint(1,range(len(self.cards)))
#        self.cards.remove(self.cards[i]);
        i = randint(0, len(self.cards) - 1)
        return self.cards.pop(i)
