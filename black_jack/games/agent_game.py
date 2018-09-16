from ..ai.reinforcement_learning.agents.random_agent import RandomAgent
from ..ai.reinforcement_learning.agents.heuristic_agent import HeuristicAgent
from .interactive_game import InteractiveGame
from ..components.player import Player
from ..components.deck import Deck


class AgentGame(InteractiveGame):
    def __init__(self, nbr_players, nbr_decks, agent_type, verbose, **agent_kwargs):
        super().__init__(nbr_players, nbr_decks, verbose)

        if agent_type == 'random':
            self.agents = [RandomAgent(player=player, **agent_kwargs) for player in self.agents]
        elif agent_type == 'heuristic':
            self.agents = [HeuristicAgent(player=player, **agent_kwargs) for player in self.agents]
        elif agent_type == 'different':
            pass

    def get_action(self, player):
        return player.action(state={'player': player, 'dealer': self.dealer})

    def play(self):
        winners = super().play()
        return winners, [player.bet() for player in self.agents]

    def reset_board(self):
        self.deck = Deck(self.nbr_decks)
        self.deck.shuffle()
        self.dealer = Player([card for card in self.deck.draw(1)])

        for agent in self.agents:
            agent.player = Player([card for card in self.deck.draw(2)])

        self.black_jacks = list()
        self.doubles = [False for _ in range(len(self.agents))]
        self.check_for_blackjack()


class MultipleAgentGame(AgentGame):
    def __init__(self, agent_configs, nbr_decks, verbose):
        self.agent_configs = agent_configs
        self.agent_type = self.check_for_different_agents(self.agent_configs)
        player_kwargs = dict()
        player_kwargs['betting_strategy'] = self.agent_configs[0]['betting_strategy']
        player_kwargs['cash'] = self.agent_configs[0]['current_cash']
        player_kwargs['actions'] = self.agent_configs[0]['possible_actions']

        super().__init__(
            nbr_players=len(self.agent_configs), nbr_decks=nbr_decks, agent_type=self.agent_type, verbose=verbose,
            **player_kwargs)

        if self.agent_type == 'different':
            self.agents = [self.init_agent(current_config, config_index) for config_index, current_config in
                           enumerate(self.agent_configs)]

    @staticmethod
    def check_for_different_agents(agent_configs):
        first_agent_type = agent_configs[0]['agent_type']
        all_same = True
        for current_agent_config in agent_configs[1:]:
            if current_agent_config['agent_type'] != first_agent_type:
                all_same = False
                break

        if all_same:
            agent_type = first_agent_type
        else:
            agent_type = 'different'

        return agent_type

    def init_agent(self, config, config_index):
        if config['agent_type'] == 'random':
            return RandomAgent(player=self.agents[config_index],
                               cash=config['current_cash'],
                               actions=config['possible_actions'],
                               betting_strategy=config['betting_strategy'])
        elif config['agent_type'] == 'heuristic':
            return HeuristicAgent(player=self.agents[config_index],
                                  cash=config['current_cash'],
                                  actions=config['possible_actions'],
                                  betting_strategy=config['betting_strategy'])
        else:
            return None
