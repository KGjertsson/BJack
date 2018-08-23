from .abstract_agent import AbstractAgent
from . import heuristic_tables


class HeuristicAgent(AbstractAgent):
    def action(self, state):
        # state: [player, dealer]
        player = state['player']
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

        return action

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
