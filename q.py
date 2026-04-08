#gen_q
# import random

# # ===== 1. Define Environment =====
# states = ["S0", "S1", "S2", "S3", "S4"]    # list of states
# actions = ["Left", "Right"]                # list of actions
# goal_state = "S4"                          # goal state
# step_cost = -1                             # step penalty
# goal_reward = 10                            # reward at goal

# # Customize number of episodes, alpha, gamma, epsilon
# num_episodes = 50
# alpha = 0.1
# gamma = 0.9
# epsilon = 0.1

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
#     Customize this function for any problem.
#     Must return next_state, reward
#     Example: move right increases index, left decreases index
#     """
#     idx = states.index(state)
#     if action == "Right":
#         next_idx = min(idx + 1, len(states) - 1)
#     else:  # "Left"
#         next_idx = max(idx - 1, 0)
    
#     next_state = states[next_idx]
#     reward = goal_reward if next_state == goal_state else step_cost
#     return next_state, reward

# # ===== 5. Q-Learning Algorithm =====
# for episode in range(1, num_episodes + 1):
#     state = states[0]  # start from initial state
    
#     while state != goal_state:
#         action = choose_action(state)
#         next_state, reward = take_action(state, action)
        
#         # Q-Learning TD target and error (off-policy)
#         td_target = reward + gamma * max(Q[next_state].values())
#         td_error = td_target - Q[state][action]
        
#         # Update Q-value
#         Q[state][action] += alpha * td_error
        
#         # Print TD error step
#         print(f"Episode {episode}, State {state}, Action {action}, TD Error {td_error:.2f}")
        
#         # Move to next state
#         state = next_state

# # ===== 6. Print final Q-values =====
# print("\nLearned Q-values:")
# for s in states:
#     print(f"State {s}: {Q[s]}")

# #------------------------------------------------------------------

# #uth_q

# import random

# # ----- Parameters -----
# Q = [[0, 0] for _ in range(5)]  # 5 states, 2 actions each
# gamma = 0.9                     # discount factor
# alpha = 0.1                     # learning rate
# num_episodes = 100

# # ----- Q-Learning Loop -----
# for episode in range(1, num_episodes + 1):
#     state = 0  # start state
    
#     while state < 4:  # until goal state
#         action = random.choice([0, 1])  # choose action randomly
#         next_state = state + 1          # transition logic
#         reward = 10 if next_state == 4 else -1  # reward function
        
#         # Q-Learning TD target and error
#         td_target = reward + gamma * max(Q[next_state])
#         td_error = td_target - Q[state][action]
#         Q[state][action] += alpha * td_error
        
#         # Optional: print TD error for exam demonstration
#         print(f"Episode {episode}, State {state}, Action {action}, TD Error {td_error:.2f}")
        
#         # Move to next state
#         state = next_state

# # ----- Print final Q-values -----
# print("\nLearned Q-values:")
# for i, qvals in enumerate(Q):
#     print(f"State {i}: {qvals}")
