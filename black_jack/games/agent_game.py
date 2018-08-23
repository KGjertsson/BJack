from ..ai.reinforcement_learning.agents.random_agent import RandomAgent
from .interactive_game import InteractiveGame


class AgentGame(InteractiveGame):
    def __init__(self, nbr_players, nbr_decks, agent_type, verbose, **agent_kwargs):
        super().__init__(nbr_players, nbr_decks, verbose)

        if agent_type == 'random':
            self.players = [RandomAgent(player=player, **agent_kwargs) for player in self.players]

    def get_action(self, player):
        return player.action(state={'player': player, 'dealer': self.dealer})
