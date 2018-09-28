from . import agent_game
from ..components.card import Card


class QLearningGame(agent_game.AgentGame):
    def perform_round(self, player, player_index):
        action = self.get_action(player)
        if action == 0:
            # hit
            player.hand += [card for card in self.deck.draw(1)]
            if self.verbose == 1:
                self.print_state()

            if player.value_of_hand() > 21:
                self.agents[player_index].update(new_state={'player': player.player, 'dealer': self.dealer},
                                                 reward=-1)
                player.hand = [Card('none', 2)]
                player.hand[0].set_value = -1
                if self.verbose == 1:
                    print('Player {} is fat'.format(player_index + 1))
                return False

            self.agents[player_index].update(new_state={'player': player.player, 'dealer': self.dealer}, reward=0)
            return self.perform_round(player, player_index)
        elif action == 1:
            # stay
            self.agents[player_index].update(new_state={'player': player.player, 'dealer': self.dealer}, reward=0)
            return True
        elif action == 2:
            # double
            player.hand += [card for card in self.deck.draw(1)]
            if self.verbose == 1:
                self.print_state()

            if player.value_of_hand() > 21:
                self.agents[player_index].update(new_state={'player': player.player, 'dealer': self.dealer}, reward=-2)
                player.hand = [Card('none', 2)]
                player.hand[0].set_value = -1
                if self.verbose == 1:
                    print('Player {} is fat'.format(player_index + 1))
                return False
            self.agents[player_index].update(new_state={'player': player.player, 'dealer': self.dealer}, reward=0)
            self.doubles[player_index] = True
            return True

        elif action == 3:
            self.init_new_players_after_split(player, player_index)
            if self.verbose == 1:
                self.print_state()
            self.agents[player_index].update(new_state={'player': player.player, 'dealer': self.dealer}, reward=0)
            return self.perform_round(player, player_index)

    def play(self):
        winners = super().play()

        for agent, winner in zip(self.agents, winners[0]):
            if winner == 1:
                reward = 1
            elif winner == 3:
                reward = 1.5
            elif winner == 4:
                reward = 2
            elif winner == 5:
                reward = -1
            elif winner == 0 and agent.player.value_of_hand() != -1:
                reward = -1
            else:
                reward = 0

            # if we get blackjack last state will never be set and errors will be thrown unless checked for
            if agent._last_state is not None:
                agent.update(new_state={'player': agent.player, 'dealer': self.dealer}, reward=reward)

        return winners
