#Generic Monte Carlo First-Visit State Value Estimation
# import random

# # ----- Define environment -----
# states = ["Good", "Partial", "Skip"]  # list of states
# rewards = {"Good": 10, "Partial": 3, "Skip": -5}  # reward at end of episode
# num_episodes = 50  # total episodes

# # ----- Initialize returns and value function -----
# returns = {state: [] for state in states}  # store all returns
# V = {state: 0 for state in states}        # estimated value

# # ----- Monte Carlo loop -----
# for episode in range(num_episodes):
#     state = random.choice(states)       # choose a state for this episode
#     G = rewards[state]                  # reward for the episode
#     returns[state].append(G)            # store return
#     V[state] = sum(returns[state]) / len(returns[state])  # average

# print("Estimated State Values:")
# print(V)

#--------------------------------------------------------------------------------------
#Monte Carlo Control (Q with ε-greedy)
# import random

# # ----- Define environment -----
# states = ["Short", "Long"]               # states
# actions = ["Fast", "Slow"]               # actions per state
# rewards = {("Short","Fast"): 5,          # reward table
#            ("Short","Slow"): 2,
#            ("Long","Fast"): 8,
#            ("Long","Slow"): 4}

# epsilon = 0.2       # exploration rate
# num_episodes = 100  # total episodes

# # ----- Initialize Q and returns -----
# Q = {state: {action: 0 for action in actions} for state in states}
# returns = {state: {action: [] for action in actions} for state in states}

# # ----- Monte Carlo loop -----
# for episode in range(num_episodes):
#     state = random.choice(states)  # pick a starting state

#     # ε-greedy action selection
#     if random.random() < epsilon:
#         action = random.choice(actions)
#     else:
#         action = max(Q[state], key=Q[state].get)

#     G = rewards[(state, action)]         # get reward
#     returns[state][action].append(G)     # store return
#     Q[state][action] = sum(returns[state][action]) / len(returns[state][action])  # average

# print("Estimated Q-values:")
# print(Q)
