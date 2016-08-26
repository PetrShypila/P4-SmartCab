import random
from clever_agent import CleverAgent


class PositiveAgent(CleverAgent):
    """
    Aplied optimism-in-face-of-uncertainty technique.
    """
    def optimal_a(self, s):
        # get q-value for each action
        qvals = { a: self.qvals.get((s, a), 10) for a in self.valid_actions }
        # collect optimal actions with max q-value
        optimal_as = [a for a in self.valid_actions if qvals[a] == max(qvals.values())]
        # choose random action of there is several with same q-value
        return random.choice(optimal_as)
