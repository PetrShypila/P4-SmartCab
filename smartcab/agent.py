import random
from environment import Agent, Environment
from planner import RoutePlanner
from simulator import Simulator

class LearningAgent(Agent):
    """An agent that learns to drive in the smartcab world."""

    def __init__(self, env):
        super(LearningAgent, self).__init__(env)  # sets self.env = env, state = None, next_waypoint = None, and a default color
        self.color = 'red'  # override color
        self.planner = RoutePlanner(self.env, self)  # simple route planner to get next_waypoint
        self.qvals = {}
        self.time = 0
        self.states = {}

    def reset(self, destination=None):
        self.planner.route_to(destination)

    def best_action(self, s):
        qvals = { a: self.qvals.get((s, a), 0) for a in Environment.valid_actions }
        best_a = [a for a in Environment.valid_actions if qvals[a] == max(qvals.values())]

        return random.choice(best_a)

    def update_qvals(self, s, a, r):
        learning_rate = 1.0/self.time
        self.qvals[(s, a)] = (1 - learning_rate) * self.qvals.get((s, a), 0) + learning_rate * r

    def update(self, t):
        self.time += 1
        # from route planner, also displayed by simulator
        self.next_waypoint = self.planner.next_waypoint()
        # gather inputs
        inputs = self.env.sense(self)
        deadline = self.env.get_deadline(self)

        # Update state
        self.state = (inputs['light'], inputs['oncoming'], inputs['left'], self.next_waypoint)
        # state visit counter
        self.states[self.state] = self.states.get(self.state, 0) + 1

        a = self.best_action(self.state)
        r = self.env.act(self, a)

        if r < 0:
            print "\npenalty!"
            print "light: {0}, oncoming: {1}, left: {2}, waypoint: {3}".format(*self.state)
            print "visit number {} to state".format(self.states[self.state])
            print "action: {}".format(a)
            print "reward: {}".format(r)

        self.update_qvals(self.state, a, r)


def run():
    """Run the agent for a finite number of trials."""

    # Set up environment and agent
    e = Environment()  # create environment (also adds some dummy traffic)
    a = e.create_agent(LearningAgent)  # create agent
    e.set_primary_agent(a, enforce_deadline=True)  # specify agent to track
    # NOTE: You can set enforce_deadline=False while debugging to allow longer trials

    # Now simulate it
    sim = Simulator(e, update_delay=0.5, display=True)  # create simulator (uses pygame when display=True, if available)
    # NOTE: To speed up simulation, reduce update_delay and/or set display=False

    sim.run(n_trials=100)  # run for a specified number of trials
    # NOTE: To quit midway, press Esc or close pygame window, or hit Ctrl+C on the command-line


if __name__ == '__main__':
    run()
