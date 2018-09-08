import numpy as np

from .abstract_agent import AbstractAgent
from . import heuristic_tables


class HeuristicAgent(AbstractAgent):
    def __init__(self, cash, actions, player, bet_strategy):
        super().__init__(cash, actions, player)
        self.bet_strategy = bet_strategy

    def action(self, state):
        # state: [player, dealer]
        player = state['player'].player
        dealer = state['dealer']

        if player.hand[0] == player.hand[1]:
            action = \
                heuristic_tables.doubles_heuristic_table[
                    dealer.hand[0].calculate_value()
                ][(player.hand[0].calculate_value(), player.hand[0].calculate_value())]
        elif player.hand[0].calculate_value() == 11:
            action = heuristic_tables.single_ace_heuristic_table[
                dealer.hand[0].calculate_value()
            ][(player.hand[0].calculate_value(), player.hand[1].calculate_value())]
        elif player.hand[1].calculate_value() == 11:
            action = heuristic_tables.single_ace_heuristic_table[
                dealer.hand[0].calculate_value()
            ][(player.hand[1].calculate_value(), player.hand[0].calculate_value())]
        else:
            action = heuristic_tables.uneven_heuristic_table[dealer.hand[0].calculate_value()][player.value_of_hand()]

        if action == 'hit':
            action = 0
        elif action == 'stay':
            action = 1
        elif action == 'double':
            # action = 2
            raise NotImplementedError('double action not yet implemented')
        elif action == 'split':
            # action = 3
            raise NotImplementedError('split action not yet implemented')

        return action

    def bet(self):
        if self.bet_strategy == 'random':
            return np.random.randint(0, self.initial_cash // 10)
        else:
            raise ValueError('Found invalid betting strategy')

    def value_of_hand(self):
        pass

    @property
    def hand(self):
        return None

    @hand.setter
    def hand(self, new_hand):
        pass
