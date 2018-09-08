import abc


class AbstractAgent(abc.ABC):
    def __init__(self, cash, actions, player):
        self.cash = cash
        self.initial_cash = cash
        self.actions = actions
        self.player = player

    @abc.abstractmethod
    def action(self, state):
        pass

    @abc.abstractmethod
    def bet(self):
        pass

    def value_of_hand(self):
        return self.player.value_of_hand()

    @property
    def hand(self):
        return None

    @hand.setter
    def hand(self, new_hand):
        pass
