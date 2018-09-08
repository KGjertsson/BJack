from ..ai.reinforcement_learning.agents.random_agent import RandomAgent
from ..ai.reinforcement_learning.agents.heuristic_agent import HeuristicAgent
from .interactive_game import InteractiveGame


class AgentGame(InteractiveGame):
    def __init__(self, nbr_players, nbr_decks, agent_type, verbose, **agent_kwargs):
        super().__init__(nbr_players, nbr_decks, verbose)

        if agent_type == 'random':
            self.agent = [RandomAgent(player=player, **agent_kwargs) for player in self.agent]
        elif agent_type == 'heuristic':
            self.agent = [HeuristicAgent(player=player, **agent_kwargs) for player in self.agent]

    def get_action(self, player):
        return player.action(state={'player': player, 'dealer': self.dealer})

    def play(self):
        winners = super().play()
        return winners, [player.bet() for player in self.agent]
