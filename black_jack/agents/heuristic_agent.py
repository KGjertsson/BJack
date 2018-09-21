from . import heuristic_tables
from .abstract_agent import AbstractAgent


class HeuristicAgent(AbstractAgent):
    def __str__(self):
        return 'HeuristicAgent'

    def action(self, state):
        # state: [player, dealer]
        player = state['player'].player
        dealer = state['dealer']

        if player.hand[0].value == player.hand[1].value:
            value = player.hand[0].calculate_value() if player.hand[0].calculate_value() != 1 else 11

            action = \
                heuristic_tables.doubles_heuristic_table[
                    dealer.hand[0].calculate_value()
                ][(value, value)]

        elif player.hand[0].calculate_value() == 11:

            dealer_value = dealer.hand[0].calculate_value()
            ace_value = player.hand[0].calculate_value()
            other_card_value = min(player.hand[1].calculate_value(), 9)
            action = heuristic_tables.single_ace_heuristic_table[dealer_value][(ace_value, other_card_value)]

        elif player.hand[1].calculate_value() == 11:

            dealer_value = dealer.hand[0].calculate_value()
            ace_value = player.hand[1].calculate_value()
            other_card_value = min(player.hand[0].calculate_value(), 9)
            action = heuristic_tables.single_ace_heuristic_table[dealer_value][(ace_value, other_card_value)]

        else:

            player_value = max(min(player.value_of_hand(), 17), 8)
            action = heuristic_tables.uneven_heuristic_table[dealer.hand[0].calculate_value()][player_value]

        if action == 'hit':
            action = 0
        elif action == 'stay':
            action = 1
        elif action == 'double':
            action = 2
        elif action == 'split':
            action = 3

        return action
