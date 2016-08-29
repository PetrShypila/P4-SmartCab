import numpy as np
from environment import Environment
from simulator import Simulator
from learner_agent import LearnerAgent


def run():
    """
    Script is used to calculate performance metrics with defferent multipliers.
    """
    trials = 100

    multipliers = [0.25, 0.3, 0.35, 0.5, 0.75, 1, 1.25, 1.45, 1.5, 1.55, 1.6] # Coefficients for learning rate

    mean_penalty = []
    median_penalty = []
    std_penalty = []

    mean_trial_time = []
    median_trial_time = []
    std_trial_time = []

    mean_success_rate = []
    median_success_rate = []
    std_success_rate = []

    for m in multipliers:
        all_penalties = [] # All penalties from trail sets
        all_average_trial_time = []
        all_success_rates = []

        for i in range(0, 20):
            # print "Trial set:", i
            # Set up environment and agent
            e = Environment()  # create environment (also adds some dummy traffic)
            agent = e.create_agent(LearnerAgent)  # create agent
            agent.mult = m
            e.set_primary_agent(agent, enforce_deadline=True)  # specify agent to track

            # Now simulate it
            sim = Simulator(e, update_delay=0.0, display=False)  # create simulator (uses pygame when display=True, if available)

            sim.run(n_trials=trials)  # run for a specified number of trials

            all_penalties.append(agent.all_trails_penalties)
            all_average_trial_time.append(agent.time/float(trials))
            all_success_rates.append(float(trials-agent.aborted_trials)/trials)

        mean_penalty.append(np.mean(all_penalties))
        median_penalty.append(np.median(all_penalties))
        std_penalty.append(np.std(all_penalties))

        mean_trial_time.append(np.mean(all_average_trial_time))
        median_trial_time.append(np.median(all_average_trial_time))
        std_trial_time.append(np.std(all_average_trial_time))

        mean_success_rate.append(np.mean(all_success_rates))
        median_success_rate.append(np.median(all_success_rates))
        std_success_rate.append(np.std(all_success_rates))

    for i in range(0, len(multipliers)):
        print ""
        print "Multiplier:", multipliers[i]
        print ""
        print "Mean penalty per {} trials:".format(trials), mean_penalty[i]
        print "Median penalty per {} trials:".format(trials), median_penalty[i]
        print "Std.Dev. penalty per {} trials:".format(trials), std_penalty[i]

        print ""
        print "Mean trial time:", mean_trial_time[i]
        print "Median trial time:", median_trial_time[i]
        print "Std.Dev. trial time:", std_trial_time[i]

        print ""
        print "Mean success rate per {} trials:".format(trials), mean_success_rate[i]
        print "Median success rate per {} trials:".format(trials), median_success_rate[i]
        print "Std.Dev. success rate per {} trials:".format(trials), std_success_rate[i]

if __name__ == '__main__':
    run()
