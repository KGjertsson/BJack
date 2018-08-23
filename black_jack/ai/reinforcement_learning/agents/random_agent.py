import numpy as np

from .abstract_agent import AbstractAgent


class RandomAgent(AbstractAgent):
    def __init__(self, cash, actions, player):
        self.cash = cash
        self.initial_cash = cash
        self.actions = actions
        self.player = player

    def action(self, state=None):
        return self.actions[np.random.randint(len(self.actions))]

    def bet(self):
        return np.random.randint(0, self.initial_cash // 10)

    def value_of_hand(self):
        return self.player.value_of_hand()

    @property
    def hand(self):
        return self.player.hand

    @hand.setter
    def hand(self, new_hand):
        self.player.hand = new_hand
