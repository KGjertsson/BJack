import numpy as np


class RandomAgent:
    def __init__(self, cash, actions, player):
        self.cash = cash
        self.actions = actions
        self.player = player

    def action(self, state=None):
        chosen_action = np.random.randint(len(self.actions))
        return chosen_action

    def value_of_hand(self):
        return self.player.value_of_hand()
