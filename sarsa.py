#gen_sar
# import random

# # ===== 1. Define Environment =====
# states = ["S0", "S1", "S2", "S3", "S4"]   # list of states
# actions = ["Left", "Right"]               # actions per state
# goal_state = "S4"                         # goal state
# step_cost = -1                             # cost per step
# goal_reward = 10                            # reward at goal
# num_episodes = 50                          # number of episodes
# gamma = 0.9                                # discount factor
# alpha = 0.1                                # learning rate
# epsilon = 0.1                              # exploration rate

# # ===== 2. Initialize Q-table =====
# Q = {s: {a: 0 for a in actions} for s in states}

# # ===== 3. ε-greedy policy =====
# def choose_action(state):
#     if random.random() < epsilon:
#         return random.choice(actions)
#     return max(Q[state], key=Q[state].get)

# # ===== 4. Define transition and reward function =====
# def take_action(state, action):
#     """
#     Customize this function for any problem!
#     Must return: next_state, reward
#     Example: move right always, reward step cost unless goal
#     """
#     idx = states.index(state)
#     if action == "Right":
#         next_idx = min(idx + 1, len(states) - 1)
#     else:  # Left or any other action
#         next_idx = max(idx - 1, 0)
#     next_state = states[next_idx]
#     reward = goal_reward if next_state == goal_state else step_cost
#     return next_state, reward

# # ===== 5. SARSA Learning =====
# for episode in range(1, num_episodes + 1):
#     state = states[0]                   # start from initial state
#     action = choose_action(state)
    
#     while state != goal_state:
#         next_state, reward = take_action(state, action)
#         next_action = choose_action(next_state)
        
#         # SARSA TD target and error
#         td_target = reward + gamma * Q[next_state][next_action]
#         td_error = td_target - Q[state][action]
#         Q[state][action] += alpha * td_error
        
#         # Print TD error
#         print(f"Episode {episode}, State {state}, Action {action}, TD Error {td_error:.2f}")
        
#         # Move to next state-action
#         state, action = next_state, next_action

# # ===== 6. Print final Q-values =====
# print("\nLearned Q-values:")
# for s in states:
#     print(f"State {s}: {Q[s]}")

# #-------------------------------------------------------------------------------------------------

# #uth_sar
# import random

# # ----- Parameters -----
# Q = [[0, 0] for _ in range(5)]  # Q-table for 5 states and 2 actions
# gamma = 0.9                     # discount factor
# alpha = 0.1                     # learning rate
# epsilon = 0.1                   # exploration rate

# # ----- ε-greedy action selection -----
# def choose_action(state):
#     if random.random() < epsilon:
#         return random.choice([0, 1])
#     return max(range(2), key=lambda a: Q[state][a])

# # ----- SARSA Learning -----
# for episode in range(100):
#     state = 0
#     action = choose_action(state)
    
#     while state < 4:  # continue until goal state
#         next_state = state + 1
#         reward = 10 if next_state == 4 else -1
#         next_action = choose_action(next_state)
        
#         # TD target and error
#         td_target = reward + gamma * Q[next_state][next_action]
#         td_error = td_target - Q[state][action]
        
#         # Q-value update
#         Q[state][action] += alpha * td_error
        
#         # Move to next state-action
#         state, action = next_state, next_action

# # ----- Print final Q-values -----
# print("Learned Q-values:")
# for i, qvals in enumerate(Q):
#     print(f"State {i}: {qvals}")
