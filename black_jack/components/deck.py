import numpy as np

from ..components.card import Card
from ..error_handling.decorators import SUITES


class Deck:
    def __init__(self, nbr_decks):

        self.cards = list()
        for _ in range(nbr_decks):
            for suite in SUITES:
                if suite != 'none':
                    for value in range(2, 15):
                        self.cards.append(Card(suite, value))

    def __str__(self):
        return str([str(card) for card in self.cards])

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        indices = np.asarray(range(self.__len__()))
        np.random.shuffle(indices)
        self.cards = [self.cards[index] for index in indices]

    def draw(self, nbr_cards):
        for _ in range(nbr_cards):
            yield self.cards.pop()
