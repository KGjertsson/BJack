from black_jack.ai.inference import play
import matplotlib.pyplot as plt

if __name__ == '__main__':
    agent_type = 'random'
    game_type = 'agent_game'
    nbr_players = 1
    nbr_decks = 6
    starting_cash = 1000
    current_cash = starting_cash
    possible_actions = [0, 1]
    verbose = 0
    betting_strategy = 'fixed'

    money_over_time = play.play_while_cash_left(current_cash,
                                                agent_type=agent_type,
                                                game_type=game_type,
                                                nbr_players=nbr_players,
                                                nbr_decks=nbr_decks,
                                                starting_cash=starting_cash,
                                                possible_actions=possible_actions,
                                                verbose=verbose,
                                                betting_strategy=betting_strategy)

    plt.show(plt.plot(money_over_time))
