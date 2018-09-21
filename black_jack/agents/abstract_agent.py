import abc

import numpy as np


class AbstractAgent(abc.ABC):
    # TODO: update architecture such that extra args aren't needed
    def __init__(self, cash, actions, player, betting_strategy):
        self.cash = cash
        self.initial_cash = cash
        self.actions = actions
        self.player = player
        self.betting_strategy = betting_strategy
        self.cash_progression = list()

    def __str__(self):
        return 'AbstractAgent'

    @abc.abstractmethod
    def action(self, state):
        pass

    def bet(self):
        if self.betting_strategy == 'random':
            return np.random.randint(50, 70)
        elif self.betting_strategy == 'fixed':
            return self.initial_cash // 100
        else:
            raise ValueError('Found invalid betting strategy')

    def value_of_hand(self):
        return self.player.value_of_hand()

    @property
    def hand(self):
        return self.player.hand

    @hand.setter
    def hand(self, new_hand):
        self.player.hand = new_hand
