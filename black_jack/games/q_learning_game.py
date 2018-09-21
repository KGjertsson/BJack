from . import agent_game


class QLearningGame(agent_game.AgentGame):
    def perform_round(self, player, player_index):
        result = super().perform_round(player, player_index)

        for agent in self.agents:
            # TODO: figure out good reward signals and how to set new state
            agent.update(new_state=1, reward=1)

        return result
