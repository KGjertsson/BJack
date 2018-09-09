from black_jack.ai.inference import play
import matplotlib.pyplot as plt

if __name__ == '__main__':
    nbr_decks = 6
    starting_cash = 1000
    verbose = 0
    heuristic_agent_config = {
        'agent_type': 'heuristic',
        'current_cash': starting_cash,
        'possible_actions': [0, 1],
        'betting_strategy': 'fixed'
    }

    random_agent_config = {
        'agent_type': 'random',
        'current_cash': starting_cash,
        'possible_actions': [0, 1],
        'betting_strategy': 'fixed'
    }

    agent_configs = [heuristic_agent_config, random_agent_config]

    money_over_time = play.play_while_cash_left_multiple_agents(
        agent_configs=agent_configs,
        nbr_decks=nbr_decks,
        verbose=verbose)

    for money in money_over_time:
        print(money.name)
        plt.plot(money.cash, label=money.name)
    plt.legend(loc="upper right")
    plt.xlabel('iteration')
    plt.ylabel('US$')
    plt.show()
