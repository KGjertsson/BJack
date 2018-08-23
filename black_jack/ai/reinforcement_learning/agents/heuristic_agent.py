from .abstract_agent import AbstractAgent

class HeuristicAgent(AbstractAgent):
    def action(self, state):
        pass

    def bet(self):
        pass

    def value_of_hand(self):
        pass

    @property
    def hand(self):
        return None

    @hand.setter
    def hand(self, new_hand):
        pass
