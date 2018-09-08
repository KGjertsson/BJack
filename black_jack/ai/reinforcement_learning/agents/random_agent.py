import numpy as np

from .abstract_agent import AbstractAgent


class RandomAgent(AbstractAgent):
    def action(self, state=None):
        return self.actions[np.random.randint(len(self.actions))]

    def bet(self):
        return np.random.randint(0, self.initial_cash // 10)
