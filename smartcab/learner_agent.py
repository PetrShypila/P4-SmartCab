from math import sqrt
from clever_agent import CleverAgent


class LearnerAgent(CleverAgent):
    """
    Agent which uses different learning rate algorithm, which is not as steep as default one.
    """
    def add_qval(self, s, a, r):
        learning_rate = 1.0/sqrt(self.time)
        self.qvals[(s, a)] = learning_rate * r + (1 - learning_rate) * self.qvals.get((s, a), 0)

