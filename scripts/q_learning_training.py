import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import pickle
import os

from black_jack import play
from black_jack.agents.q_learning_agent import QLearner
from black_jack.games import q_learning_game

if __name__ == '__main__':
    number_iterations = 1000
    verbose = 0
    plot_figures = False
    nbr_decks = 6
    starting_cash = 1000
    performance = list()
    agents = None
    results_file = 'results.pkl'
    training_progress = list()

    for _ in range(number_iterations):

        if os.path.isfile(results_file):
            with open(results_file, 'rb') as f:
                Q = pickle.load(f)
        else:
            Q = None

        agent_configs = [{
            'agent_type': QLearner,
            'alpha': 0.1,
            'epsilon': 0.1,
            'gamma': 0.1,
            'learning_rate': 0.1,
            'cash': starting_cash,
            'actions': [0, 1, 2, 3],
            'betting_strategy': 'fixed',
            'init_Q': Q
        }]

        agents = play.play_while_cash_left(
            agent_configs=agent_configs,
            nbr_decks=nbr_decks,
            verbose=verbose,
            game_cls=q_learning_game.QLearningGame)

        performance.append([{'cash': agent.cash_progression, 'name': str(agent)} for agent in agents])
        print('length of current run: {}'.format(len(agents[0].cash_progression)))
        training_progress.append(len(agents[0].cash_progression))

    with open(results_file, 'wb') as f:
        pickle.dump(agents[0]._Q, f)

    plt.show(plt.plot(training_progress))
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
