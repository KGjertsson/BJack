from .card import Card
from random import *

class Deck():
    
    n_cards = 0
    cards = []
    
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
            
    def pull_card(self):
        i = randint(0, len(self.cards) - 1)
        return self.cards.pop(i)
