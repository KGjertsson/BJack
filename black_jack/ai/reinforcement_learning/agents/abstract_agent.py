from abc import ABC, abstractmethod


class AbstractAgent(ABC):
    @abstractmethod
    def action(self, state):
        pass

    @abstractmethod
    def bet(self):
        pass

    @abstractmethod
    def value_of_hand(self):
        pass

    @abstractmethod
    @property
    def hand(self):
        pass

    @abstractmethod
    @hand.setter
    def hand(self, new_hand):
        pass
