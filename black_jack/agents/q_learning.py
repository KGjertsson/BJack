import numpy as np

from black_jack.agents.abstract_agent import AbstractAgent


class Qlearner:
    """
    State representation:
        - agent's current point total
        - value of dealer's face up card
        - whether the hand is soft
        (- whether the hand can be split)

    Actions:
        - hit
        - stay
        (- split)
        (- double down)

    Reward system:
        For each action that does not result in a transition to a terminal state, a reward of 0 is given.
        Once a terminal state has been reached, a reward is given based on the size of the agent's bet. I.e.
        +given_bet if the agent won and -given_bet if the agent lost.  
    """

    def __init__(self, alpha, epsilon, gamma):
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma


class Learner(AbstractAgent):
    def __init__(self, alpha, epsilon, gamma, learning_rate, **player_init_kwargs):
        super().__init__(**player_init_kwargs)
        self._Q = {}
        self.alpha = alpha
        self.epsilon = epsilon
        self.gamma = gamma
        self.learning_rate = learning_rate

        self._last_state = None
        self._last_action = None
        self._learning = True

    def action(self, state):
        if state in self._Q and np.random.uniform(0, 1) >= self.epsilon:
            action = max(self._Q[state], key=self._Q[state].get)
        else:
            action = np.random.choice(self.actions)

        if state not in self._Q:
            self._Q[state] = {}
        self._Q[state][action] = 0

        self._last_state = state
        self._last_action = action

        return action

    def update(self, new_state, reward):
        if self._learning:
            old = self._Q[self._last_state][self._last_action]

            if new_state in self._Q:
                new = self.gamma * \
                      self._Q[new_state][max(self._Q[new_state], key=self._Q[new_state].get)]
            else:
                new = 0

            self._Q[self._last_state][self._last_action] = \
                (1 - self.learning_rate) * old + self.learning_rate * (reward + new)
