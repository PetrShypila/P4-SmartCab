import random
from random_agent import RandomAgent


class CleverAgent(RandomAgent):

    def optimal_a(self, s):
        # get q-value for each action
        qvals = { a: self.qvals.get((s, a), 0) for a in self.valid_actions }
        # collect optimal actions with max q-value
        optimal_as = [a for a in self.valid_actions if qvals[a] == max(qvals.values())]
        # choose random action of there is several with same q-value
        return random.choice(optimal_as)

    def add_qval(self, s, a, r):
        learning_rate = 1.0/self.time
        self.qvals[(s, a)] = learning_rate * r + (1 - learning_rate) * self.qvals.get((s, a), 0)

