from .interactive_game import InteractiveGame
from ..components.player import Player


class AgentGame(InteractiveGame):
    def __init__(self, agent_kwargs, nbr_decks, verbose):
        super().__init__(len(agent_kwargs), nbr_decks, verbose)

        self.agent_classes = [agent_kwarg.pop('agent_type') for agent_kwarg in agent_kwargs]
        self.agents = [agent(player=player, **agent_kwarg) for player, agent_kwarg, agent in
                       zip(self.agents, agent_kwargs, self.agent_classes)]
        self.agent_kwargs = agent_kwargs

    def get_action(self, player):
        return player.action(state={'player': player.player, 'dealer': self.dealer})

    def play(self):
        winners = super().play()
        return winners, [player.bet() for player in self.agents], [agent.player.ancestor_index for agent in self.agents]

    def reset_agents(self):
        child_agents = list()
        for agent_index, agent in enumerate(self.agents):
            if agent.player.ancestor_index is not None:
                child_agents = [agent_index] + child_agents

        for agent_index in child_agents:
            self.agents.pop(agent_index)

        for agent in self.agents:
            agent.player = Player([card for card in self.deck.draw(2)])

    def init_new_players_after_split(self, player, player_index):
        new_player = Player([player.player.hand[1]])
        new_player.hand.append([card for card in self.deck.draw(1)][0])
        new_player.ancestor_index = player_index if player.player.ancestor_index is None \
            else player.player.ancestor_index

        class_index = player_index if player.player.ancestor_index is None \
            else player.player.ancestor_index
        self.agents.append(self.agent_classes[class_index](player=new_player, **self.agent_kwargs[0]))

        player.player.hand = [player.player.hand[0]]
        player.player.hand.append([card for card in self.deck.draw(1)][0])
        self.doubles.append(False)
