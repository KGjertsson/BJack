from .interactive_game import InteractiveGame


class AgentGame(InteractiveGame):
    def __init__(self, nbr_players, nbr_decks, players):
        super().__init__(nbr_players, nbr_decks)
        self.players = players

    def perform_round(self, player, player_index):
        pass
