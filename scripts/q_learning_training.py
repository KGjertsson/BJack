import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

from black_jack import play
from black_jack.agents.q_learning_agent import QLearner
from black_jack.games import q_learning_game

if __name__ == '__main__':
    number_iterations = 1
    verbose = 0
    plot_figures = True
    nbr_decks = 6
    starting_cash = 1000
    performance = list()

    for _ in tqdm(range(number_iterations)):
        agent_configs = [{
            'agent_type': QLearner,
            'alpha': 0.1,
            'epsilon': 0.1,
            'gamma': 0.1,
            'learning_rate': 0.1,
            'cash': starting_cash,
            'actions': [0, 1, 2, 3],
            'betting_strategy': 'fixed'
        }]

        agents = play.play_while_cash_left(
            agent_configs=agent_configs,
            nbr_decks=nbr_decks,
            verbose=verbose,
            game_cls=q_learning_game.QLearningGame)

        performance.append([{'cash': agent.cash_progression, 'name': str(agent)} for agent in agents])

    print('-')
    print('-')
    print('-')
    print(np.mean([nbr_rounds for nbr_rounds in
                   [[len(agent['cash']) for agent in bj_round] for bj_round in performance]]))

    if plot_figures:
        for agents in performance:
            for money in agents:
                plt.plot(money['cash'], label=money['name'])
        plt.legend(loc="upper right")
        plt.xlabel('iteration')
        plt.ylabel('US$')
        plt.show()
