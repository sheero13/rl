# #Explore State and Action Spaces\

# import gymnasium as gym

# # Create the Cliff Walking environment
# env = gym.make('CliffWalking-v0')

# # Compute the size of the action space
# num_actions = env.action_space.n

# # Compute the size of the state space
# num_states = env.observation_space.n

# print("Number of actions:", num_actions)
# print("Number of states:", num_states)
# #--------------------------------------------------------------------------------
# #Investigate Transition Probabilities and Rewards

# # Choose a specific state to inspect
# state = 35

# # Extract transitions for each state-action pair
# for action in range(num_actions):
#     transitions = env.unwrapped.P[state][action]
#     for transition in transitions:
#         probability, next_state, reward, done = transition
#         print(f"Action {action} -> Probability: {probability}, Next State: {next_state}, Reward: {reward}, Done: {done}")
    
# #---------------------------------------------------------------------------------
# #Define a Deterministic Policy and Execute It

# # Custom environment: MyGridWorld
# env = gym.make('MyGridWorld', render_mode='rgb_array')
# state, info = env.reset()

# # Define deterministic policy (state -> action)
# # Actions: 0=left, 1=down, 2=right, 3=up
# policy = {0:2, 1:2, 2:1, 3:1, 4:0, 5:0, 6:2, 7:2}

# terminated = False
# while not terminated:
#     # Choose action based on policy
#     action = policy[state]
    
#     # Take step in environment
#     state, reward, terminated, truncated, info = env.step(action)
    
#     # Render environment
#     env.render()

# #----------------------------------------------------------------------------------
# # v(s) computation for policy

# gamma = 0.9                   # discount factor
# terminal_state = max(policy)   # assuming last state is terminal, adjust if needed

# # Recursive function to compute V(s) under deterministic policy
# def compute_state_value(state):
#     if state == terminal_state:
#         return 0
#     action = policy[state]
#     # Get next state and reward from environment dynamics
#     _, next_state, reward, _ = env.unwrapped.P[state][action][0]
#     return reward + gamma * compute_state_value(next_state)

# # Compute state-values for all states
# num_states = env.observation_space.n
# state_values = {state: compute_state_value(state) for state in range(num_states)}

# print("State Values under policy:")
# for s, v in state_values.items():
#     print(f"State {s}: {v:.2f}")
