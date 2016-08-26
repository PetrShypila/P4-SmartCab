import sys, random_agent, clever_agent, positive_agent, learner_agent
import numpy as np
from environment import Environment
from simulator import Simulator


def run(class_name):
    """Run the agent for a finite number of trials."""
    trials = 100
    all_penalties = []
    all_average_trial_time = []
    all_success_rates = []

    for x in range(0, 20):
        print "Trial:", x
        # Set up environment and agent
        e = Environment()  # create environment (also adds some dummy traffic)
        agent_class = eval(class_name)
        agent = e.create_agent(agent_class)  # create agent
        e.set_primary_agent(agent, enforce_deadline=True)  # specify agent to track

        # Now simulate it
        sim = Simulator(e, update_delay=0.0, display=False)  # create simulator (uses pygame when display=True, if available)

        sim.run(n_trials=trials)  # run for a specified number of trials

        all_penalties.append(agent.penalties)
        all_average_trial_time.append(agent.time/float(trials))
        all_success_rates.append(float(trials-agent.aborted_trials)/trials)

    print ""
    print "Mean penalty per {} trials:".format(trials), np.mean(all_penalties)
    print "Std.Dev. penalty per {} trials:".format(trials), np.std(all_penalties)
    print ""
    print "Mean trial time:", np.mean(all_average_trial_time)
    print "Std.Dev. trial time:", np.std(all_average_trial_time)
    print ""
    print "Mean success rate per {} trials:".format(trials), np.mean(all_success_rates)
    print "Std.Dev. success rate per {} trials:".format(trials), np.std(all_success_rates)

if __name__ == '__main__':
    run(sys.argv[1])
