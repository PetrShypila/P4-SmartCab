**QUESTION 1:**
_Observe what you see with the agent's behavior as it takes random actions. Does the **smartcab** eventually make it to the destination? Are there any other interesting observations to note?_

**ANSWER 1:**
Unfortunately agent with random behaviour didn't reach a destination. Each action of the agent returned with positive or negative reward.
And the interesting part is that overall reward in general stayed near 0. Sometimes it was higher than 0, sometimes lower. But I would say that mean value is zero.

**QUESTION 2:**
_
What states have you identified that are appropriate for modeling the **smartcab** and environment?
Why do you believe each of these states to be appropriate for this problem?_

**ANSWER 2:**
Here are a list of appropriate states for modeling the smartcab and environment:
1. Light. Possible states: Green, Red. Green light means that agent can perform next action with exception on left turn. Red light means that agent cannot perform action with exception on right turn.
2. Oncoming. Possible states: None, forward, left, right. Defines whether there is oncoming traffic or not and which direction it goes. With oncoming traffic agent may not turn left with green light or turn right with red light.
3. Right. Possible states: None, forward, left, right. Defines whether there is traffic from the right of the agent or not and which direction it goes. Right-of-way rules don't take right-side traffic into account so this property is unnecessary.
4. Left. Possible states: None, forward, left, right. Defines whether there is traffic from the left of the agent or not and which direction it goes. Traffic from left going forward means that agent cannot turn right on red light.
5. Next waypoint. Possible states: forward, left, right. Defines which direction agent should go to reach the destination. Without this feature agent won't know where to go.
6. Deadline. Meaningless feature since agent looks for optimal route without taking deadline state into account. This feature cannot force agent make other decision.

So the state will consists of 4 features(Light(Red, Green), Oncoming(None, forward, left, right), Left(None, forward, left, right), Next waypoint(forward, left, right)). By counting them we get 2*4*4*3=96. So we are interested in 96 unique states.
An overall amount of all possible states is equal to 2*4*4*4*3=384 multiplied by amount of all possible states of Deadline feature. Such a big number of states doesn't seems reasonable since it requires much more calculation.

