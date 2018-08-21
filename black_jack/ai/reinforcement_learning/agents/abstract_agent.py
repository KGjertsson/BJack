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
    def hand(self):
        pass
