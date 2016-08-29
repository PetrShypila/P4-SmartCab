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
    all_optimal_trails_percentage = []
    lowerq_optimal_trail_percentage = []
    upperq_optimal_trail_percentage = []

    print class_name, "agent is chosen"

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

        all_penalties.append(agent.all_trails_penalties) # Overall amount of penalties per trial
        all_average_trial_time.append(agent.time/float(trials)) # Average amount of time spent per trial
        all_success_rates.append(float(trials-agent.aborted_trials)/trials) # Successful trails percentage

        all_optimal_trails_percentage.append(float(agent.trail_optimal_policy.count(True))/len(agent.trail_optimal_policy)) # Percentage of trials without penalties.

        lowerq_opt_policy = agent.trail_optimal_policy[:int(trials*0.25)]
        lowerq_optimal_trail_percentage.append(float(lowerq_opt_policy.count(True))/len(lowerq_opt_policy)) # Percentage of trials without penalties for lower quartile.

        upperq_opt_policy = agent.trail_optimal_policy[int(trials*0.75):]
        upperq_optimal_trail_percentage.append(float(upperq_opt_policy.count(True))/len(upperq_opt_policy)) # Percentage of trials without penalties.

    print ""
    print "Mean penalty per {} trials:".format(trials), np.mean(all_penalties)
    print "Median penalty per {} trials:".format(trials), np.median(all_penalties)
    print "Std.Dev. penalty per {} trials:".format(trials), np.std(all_penalties)
    print ""
    print "Mean trial time:", np.mean(all_average_trial_time)
    print "Median trial time:", np.mean(all_average_trial_time)
    print "Std.Dev. trial time:", np.std(all_average_trial_time)
    print ""
    print "Mean success rate per {} trials:".format(trials), np.mean(all_success_rates)
    print "Median success rate per {} trials:".format(trials), np.median(all_success_rates)
    print "Std.Dev. success rate per {} trials:".format(trials), np.std(all_success_rates)
    print ""
    print "*** OPTIMAL POLICY STATISTICS ***"
    print "Mean relation of trails without penalties:", np.mean(all_optimal_trails_percentage)
    print "Median relation of trails without penalties:", np.median(all_optimal_trails_percentage)
    print "Std.Dev. relation of trails without penalties:", np.std(all_optimal_trails_percentage)
    print ""
    print "Mean relation of trails without penalties for lower quartile:", np.mean(lowerq_optimal_trail_percentage)
    print "Median relation of trails without penalties for lower quartile:", np.median(lowerq_optimal_trail_percentage)
    print "Std.Dev. relation of trails without penalties for lower quartile:", np.std(lowerq_optimal_trail_percentage)
    print ""
    print "Mean relation of trails without penalties for upper quartile:", np.mean(upperq_optimal_trail_percentage)
    print "Median relation of trails without penalties for upper quartile:", np.median(upperq_optimal_trail_percentage)
    print "Std.Dev. relation of trails without penalties for upper quartile:", np.std(upperq_optimal_trail_percentage)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        sys.argv.append("learner_agent.LearnerAgent")
    run(sys.argv[1])
