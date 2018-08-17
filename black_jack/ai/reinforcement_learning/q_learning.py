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
