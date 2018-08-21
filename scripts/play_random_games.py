from black_jack.ai.inference import play

if __name__ == '__main__':
    for _ in range(10):
        agent_type = 'random'
        game_type = 'agent_game'
        nbr_players = 1
        nbr_decks = 6
        starting_cash = 1000
        possible_actions = [0, 1]
        verbose = 0

        play.play_game(agent_type, game_type, nbr_players, nbr_decks, starting_cash, possible_actions, verbose)
