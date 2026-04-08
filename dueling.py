# lineworld

# import gymnasium as gym
# from gymnasium import spaces
# import numpy as np
# import torch
# import torch.nn as nn
# from stable_baselines3 import DQN
# from stable_baselines3.dqn.policies import DQNPolicy

# # -------- CUSTOM ENV --------
# class LineWorldEnv(gym.Env):
#     def __init__(self):
#         super().__init__()
#         self.observation_space = spaces.Box(low=0, high=1, shape=(5,), dtype=np.float32)
#         self.action_space = spaces.Discrete(2)
#         self.state = 2

#     def one_hot(self, state):
#         vec = np.zeros(5, dtype=np.float32)
#         vec[state] = 1.0
#         return vec

#     def reset(self, seed=None, options=None):
#         self.state = 2
#         return self.one_hot(self.state), {}

#     def step(self, action):
#         if action == 0:
#             self.state -= 1
#         else:
#             self.state += 1

#         if self.state == 4:
#             return self.one_hot(self.state), 1.0, True, False, {}
#         if self.state == 0:
#             return self.one_hot(self.state), 0.0, True, False, {}

#         return self.one_hot(self.state), 0.0, False, False, {}

# # -------- DUELING NETWORK --------
# class DuelingQNetwork(nn.Module):
#     def __init__(self, input_dim, action_dim):
#         super().__init__()

#         self.feature = nn.Sequential(
#             nn.Linear(input_dim, 16),
#             nn.ReLU()
#         )

#         self.value_stream = nn.Linear(16, 1)
#         self.advantage_stream = nn.Linear(16, action_dim)

#     def forward(self, x):
#         if x.dim() == 1:
#             x = x.unsqueeze(0)

#         x = self.feature(x)
#         value = self.value_stream(x)
#         advantage = self.advantage_stream(x)

#         return value + (advantage - advantage.mean(dim=1, keepdim=True))

#     # Required by SB3
#     def set_training_mode(self, mode: bool):
#         self.train(mode)

#     # Required by SB3
#     def _predict(self, observation, deterministic=True):
#         q_values = self.forward(observation)
#         return torch.argmax(q_values, dim=1)

# # -------- CUSTOM POLICY --------
# class DuelingDQNPolicy(DQNPolicy):
#     def make_q_net(self):
#         input_dim = self.observation_space.shape[0]
#         action_dim = self.action_space.n
#         return DuelingQNetwork(input_dim, action_dim)

# # -------- TRAIN --------
# env = LineWorldEnv()

# model = DQN(
#     policy=DuelingDQNPolicy,
#     env=env,
#     learning_rate=1e-3,
#     buffer_size=10000,
#     learning_starts=100,
#     batch_size=32,
#     gamma=0.9,
#     verbose=0
# )

# model.learn(total_timesteps=5000)

# print("\nDueling DQN Training Completed!\n")

# # -------- PRINT Q-VALUES --------
# print("Learned Q-values:\n")

# for state in range(5):
#     obs = env.one_hot(state)
#     obs_tensor = torch.tensor(obs, dtype=torch.float32)

#     with torch.no_grad():
#         q_values = model.q_net(obs_tensor)

#     print(f"State {state}: {q_values.numpy()}")

# # -------- BEST ACTIONS --------
# print("\nBest actions per state:\n")

# for state in range(5):
#     obs = env.one_hot(state)
#     action, _ = model.predict(obs, deterministic=True)
#     print(f"State {state} -> Best Action: {action}")


#--------------------------------------------------------------------------------------

#custom

# pip install stable-baselines3 gymnasium torch

# import gymnasium as gym
# import numpy as np
# import torch
# import torch.nn as nn
# from gymnasium import spaces
# from stable_baselines3 import DQN
# from stable_baselines3.dqn.policies import DQNPolicy

# # -------- UNIVERSAL OBS HANDLER --------
# def flatten_obs(obs):
#     return np.array(obs, dtype=np.float32).flatten()

# # -------- HANDLE DISCRETE OBS (ONE-HOT) --------
# def wrap_env(env):
#     if isinstance(env.observation_space, spaces.Discrete):
#         n = env.observation_space.n

#         class OneHotWrapper(gym.ObservationWrapper):
#             def __init__(self, env):
#                 super().__init__(env)
#                 self.observation_space = spaces.Box(low=0, high=1, shape=(n,), dtype=np.float32)

#             def observation(self, obs):
#                 vec = np.zeros(n, dtype=np.float32)
#                 vec[obs] = 1.0
#                 return vec

#         env = OneHotWrapper(env)

#     return env

# # -------- DUELING NETWORK --------
# class DuelingQNetwork(nn.Module):
#     def __init__(self, input_dim, action_dim):
#         super().__init__()

#         self.feature = nn.Sequential(
#             nn.Linear(input_dim, 64),
#             nn.ReLU()
#         )

#         self.value = nn.Linear(64, 1)
#         self.advantage = nn.Linear(64, action_dim)

#     def forward(self, x):
#         if not isinstance(x, torch.Tensor):
#             x = torch.tensor(x, dtype=torch.float32)

#         if x.dim() == 1:
#             x = x.unsqueeze(0)

#         x = self.feature(x)

#         value = self.value(x)
#         advantage = self.advantage(x)

#         return value + (advantage - advantage.mean(dim=1, keepdim=True))

#     def set_training_mode(self, mode: bool):
#         self.train(mode)

#     def _predict(self, observation, deterministic=True):
#         q_values = self.forward(observation)
#         return torch.argmax(q_values, dim=1)

# # -------- CUSTOM POLICY --------
# class DuelingPolicy(DQNPolicy):
#     def make_q_net(self):
#         input_dim = int(np.prod(self.observation_space.shape))
#         action_dim = self.action_space.n
#         return DuelingQNetwork(input_dim, action_dim)

# # -------- CHOOSE ENV --------
# # CHANGE ONLY THIS LINE IN EXAM

# env = gym.make("CartPole-v1")
# #env = gym.make("FrozenLake-v1", is_slippery=False)

# # -------- PREPROCESS ENV --------
# env = wrap_env(env)

# # -------- MODEL --------
# model = DQN(
#     policy=DuelingPolicy,
#     env=env,
#     learning_rate=1e-3,
#     buffer_size=10000,
#     learning_starts=100,
#     batch_size=32,
#     gamma=0.99,
#     verbose=0
# )

# # -------- TRAIN --------
# model.learn(total_timesteps=5000)

# print("\nDueling DQN Training Completed!\n")

# # -------- PRINT Q VALUES --------
# print("Sample Q-values:\n")

# obs, _ = env.reset()

# for i in range(5):
#     obs_flat = flatten_obs(obs)
#     obs_tensor = torch.tensor(obs_flat, dtype=torch.float32)

#     with torch.no_grad():
#         q_values = model.q_net(obs_tensor)

#     print(f"Step {i}: Q-values = {q_values.numpy()}")

#     action, _ = model.predict(obs, deterministic=True)
#     obs, _, done, truncated, _ = env.step(action)

#     if done or truncated:
#         obs, _ = env.reset()

# # -------- BEST ACTION DEMO --------
# print("\nBest actions:\n")

# obs, _ = env.reset()

# for i in range(10):
#     action, _ = model.predict(obs, deterministic=True)
#     print(f"Step {i}: Action = {action}")
#     obs, _, done, truncated, _ = env.step(action)

#     if done or truncated:
#         obs, _ = env.reset()
