import numpy as np

from .abstract_agent import AbstractAgent


class RandomAgent(AbstractAgent):
    def __str__(self):
        return 'RandomAgent'

    def action(self, state=None):
        return self.actions[np.random.randint(len(self.actions))]
