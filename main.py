# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 22:36:40 2016
"""

from classes.card import Card
from classes.deck import Deck
#
#card1 = Card(1, 1)
#card2 = Card(2, 2)
#card1.displayCard()
#card2.displayCard()

deck = Deck(1)
print("length is", len(deck.cards))
print("pulled card is:", deck.pullCard())