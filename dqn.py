# sb3_custom_env

# import gymnasium as gym
# from gymnasium import spaces
# import numpy as np
# import torch
# from stable_baselines3 import DQN

# # -------- CUSTOM ENV --------
# class LineWorldEnv(gym.Env):
#     def __init__(self):
#         super().__init__()
#         self.observation_space = spaces.Discrete(5)
#         self.action_space = spaces.Discrete(2)
#         self.state = 2

#     def reset(self, seed=None, options=None):
#         super().reset(seed=seed)
#         self.state = 2
#         return self.state, {}

#     def step(self, action):
#         if action == 0:
#             self.state -= 1
#         else:
#             self.state += 1

#         # Keep state within bounds
#         self.state = np.clip(self.state, 0, 4)

#         if self.state == 4:
#             return self.state, 1.0, True, False, {}
#         if self.state == 0:
#             return self.state, 0.0, True, False, {}

#         return self.state, 0.0, False, False, {}

# # -------- CREATE ENV --------
# env = LineWorldEnv()

# # -------- CREATE MODEL --------
# model = DQN(
#     policy="MlpPolicy",
#     env=env,
#     learning_rate=0.01,
#     buffer_size=1000,
#     learning_starts=100,
#     batch_size=16,
#     gamma=0.9,
#     train_freq=1,
#     target_update_interval=20,
#     verbose=0
# )

# # -------- TRAIN --------
# model.learn(total_timesteps=5000)

# print("DQN Training Completed!\n")

# # -------- PRINT Q-VALUES --------
# print("Learned Q-values:")

# for state in range(5):
#     obs = np.array([state])

#     # Convert to tensor (batch format)
#     obs_tensor = torch.tensor(obs).float().unsqueeze(0)

#     with torch.no_grad():
#         q_values = model.q_net(obs_tensor)

#     print(f"State {state}: {q_values.numpy()[0]}")

# # -------- PRINT BEST ACTION --------
# print("\nBest actions per state:")

# for state in range(5):
#     obs = np.array([state])
#     action, _ = model.predict(obs, deterministic=True)
#     print(f"State {state} -> Best Action: {action}")


#--------------------------------------------------------------------------------

#uth_ddqn

# import random
# import numpy as np
# import torch
# import torch.nn as nn
# import torch.optim as optim

# # ---------------- ENVIRONMENT ----------------
# class LineWorld:
#     def reset(self):
#         self.state = 2
#         return self.state

#     def step(self, action):
#         self.state += -1 if action == 0 else 1

#         if self.state == 4:
#             return self.state, 1.0, True
#         if self.state == 0:
#             return self.state, 0.0, True

#         return self.state, 0.0, False

# # -------------- STATE ENCODING ---------------
# def one_hot(state):
#     x = np.zeros(5)
#     x[state] = 1
#     return torch.tensor(x, dtype=torch.float32)

# # ---------------- DQN MODEL ------------------
# class DQN(nn.Module):
#     def __init__(self):
#         super().__init__()
#         self.fc1 = nn.Linear(5, 16)
#         self.fc2 = nn.Linear(16, 2)

#     def forward(self, x):
#         return self.fc2(torch.relu(self.fc1(x)))

# # ------------- REPLAY BUFFER -----------------
# class ReplayBuffer:
#     def __init__(self):
#         self.buffer = []

#     def push(self, t):
#         if len(self.buffer) > 1000:
#             self.buffer.pop(0)
#         self.buffer.append(t)

#     def sample(self, n):
#         return random.sample(self.buffer, n)

# # ---------------- TRAINING -------------------
# env = LineWorld()
# q_net = DQN()
# target_net = DQN()
# target_net.load_state_dict(q_net.state_dict())

# optimizer = optim.Adam(q_net.parameters(), lr=0.01)

# buffer = ReplayBuffer()

# gamma = 0.9
# epsilon = 0.2
# batch_size = 16
# steps = 0

# for episode in range(300):
#     state = env.reset()
#     done = False

#     while not done:
#         steps += 1
#         s = one_hot(state)

#         # ε-greedy action selection
#         if random.random() < epsilon:
#             action = random.randint(0, 1)
#         else:
#             action = torch.argmax(q_net(s)).item()

#         next_state, reward, done = env.step(action)

#         buffer.push((state, action, reward, next_state, done))
#         state = next_state

#         if len(buffer.buffer) < batch_size:
#             continue

#         batch = buffer.sample(batch_size)
#         loss = 0

#         for s, a, r, s_next, d in batch:
#             s_t = one_hot(s)
#             s_next_t = one_hot(s_next)

#             q_sa = q_net(s_t)[a]

#             with torch.no_grad():
#                 # -------- DDQN TARGET --------
#                 best_action = torch.argmax(q_net(s_next_t)).item()
#                 target_q = target_net(s_next_t)[best_action]
#                 y = r if d else r + gamma * target_q

#             loss += (y - q_sa) ** 2

#         loss = loss / batch_size

#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#         # Update target network
#         if steps % 20 == 0:
#             target_net.load_state_dict(q_net.state_dict())

# print("Double DQN training completed")

#-------------------------------------------------------------------------------

#uth_dqn

# pip install stable-baselines3 gymnasium torch

# import gymnasium as gym
# from gymnasium import spaces
# import numpy as np
# import torch
# from stable_baselines3 import DQN

# # -------- CUSTOM ENV --------
# class LineWorldEnv(gym.Env):
#     def __init__(self):
#         super().__init__()
#         self.observation_space = spaces.Discrete(5)
#         self.action_space = spaces.Discrete(2)
#         self.state = 2

#     def reset(self, seed=None, options=None):
#         self.state = 2
#         return self.state, {}

#     def step(self, action):
#         if action == 0:
#             self.state -= 1
#         else:
#             self.state += 1

#         if self.state == 4:
#             return self.state, 1.0, True, False, {}
#         if self.state == 0:
#             return self.state, 0.0, True, False, {}

#         return self.state, 0.0, False, False, {}

# # -------- TRAIN --------
# env = LineWorldEnv()

# model = DQN(
#     "MlpPolicy",
#     env,
#     learning_rate=1e-3,
#     buffer_size=10000,
#     learning_starts=100,
#     batch_size=32,
#     gamma=0.9,
#     verbose=0
# )

# model.learn(total_timesteps=5000)

# print("DQN / DDQN Training Completed!\n")

# # -------- PRINT Q-VALUES --------
# print("Learned Q-values:")

# for state in range(5):
#     obs = np.array([state])
#     obs_tensor = torch.tensor(obs, dtype=torch.float32)

#     with torch.no_grad():
#         q_values = model.q_net(obs_tensor)

#     print(f"State {state}: {q_values.numpy()}")

# # -------- BEST ACTIONS --------
# print("\nBest actions per state:")

# for state in range(5):
#     obs = np.array([state])
#     action, _ = model.predict(obs, deterministic=True)
#     print(f"State {state} -> Best Action: {action}")
