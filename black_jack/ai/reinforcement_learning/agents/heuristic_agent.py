import numpy as np

from .abstract_agent import AbstractAgent
from . import heuristic_tables


class HeuristicAgent(AbstractAgent):
    def __init__(self, cash, actions, player, betting_strategy):
        super().__init__(cash, actions, player)
        self.betting_strategy = betting_strategy

    def action(self, state):
        # state: [player, dealer]
        player = state['player'].player
        dealer = state['dealer']

        # TODO: fix occasional key errors
        if player.hand[0] == player.hand[1]:
            action = \
                heuristic_tables.doubles_heuristic_table[
                    dealer.hand[0].calculate_value()
                ][(player.hand[0].calculate_value(), player.hand[0].calculate_value())]
        # TODO: fix occasional key errors
        elif player.hand[0].calculate_value() == 11:
            action = heuristic_tables.single_ace_heuristic_table[
                dealer.hand[0].calculate_value()
            ][(player.hand[0].calculate_value(), player.hand[1].calculate_value())]
        # TODO: fix occasional key errors
        elif player.hand[1].calculate_value() == 11:
            action = heuristic_tables.single_ace_heuristic_table[
                dealer.hand[0].calculate_value()
            ][(player.hand[1].calculate_value(), player.hand[0].calculate_value())]
        else:
            player_value = max(min(player.value_of_hand(), 17), 8)
            action = heuristic_tables.uneven_heuristic_table[dealer.hand[0].calculate_value()][player_value]

        if action == 'hit':
            action = 0
        elif action == 'stay':
            action = 1
        elif action == 'double':
            action = 0
            # TODO: implement, currently using hit
        elif action == 'split':
            # TODO: implement, currently using hit
            action = 0

        return action

    def bet(self):
        if self.betting_strategy == 'random':
            # TODO: implement proper strategy here
            # return np.random.randint(0, self.initial_cash // 10)
            return np.random.randint(50, 70)
        else:
            raise ValueError('Found invalid betting strategy')
