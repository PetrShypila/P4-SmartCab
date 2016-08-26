import random
from environment import Agent, Environment
from planner import RoutePlanner

class RandomAgent(Agent):
    """A simple agent which chooses actions randomly."""

    def __init__(self, env):
        super(RandomAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        self.qvals = {}
        self.time = 0.0
        self.penalties = 0.0
        self.aborted_trials = 0.0
        self.valid_actions = Environment.valid_actions

    def reset(self, destination=None):
        self.planner.route_to(destination)

    def optimal_a(self, state):
        return random.choice(self.valid_actions)

    def add_qval(self, s, a, r):
        self.qvals[(s, a)] = 0

    def update(self, t):
        self.time += 1.0
        # from route planner, also displayed by simulator
        self.next_waypoint = self.planner.next_waypoint()
        # gather inputs
        inputs = self.env.sense(self)

        # Update state
        self.state = (inputs['light'], inputs['oncoming'], inputs['left'], self.next_waypoint)

        # choose optimal action
        a = self.optimal_a(self.state)
        # Get a reward
        r = self.env.act(self, a)
        # calculate q-value
        self.add_qval(self.state, a, r)

        if r < 0:
            self.penalties += 1.0