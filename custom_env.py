# class OneDGoalEnv(gym.Env):
#     def __init__(self):
#         super().__init__()
#         self.observation_space = spaces.Discrete(11)  # 0 to 10
#         self.action_space = spaces.Discrete(2)
#         self.state = 0

#     def reset(self, seed=None, options=None):
#         self.state = 0
#         return self.state, {}

#     def step(self, action):
#         if action == 0:
#             self.state -= 1
#         else:
#             self.state += 1

#         self.state = np.clip(self.state, 0, 10)

#         reward = 10 if self.state == 10 else 0
#         done = self.state == 10

#         return self.state, reward, done, False, {}
    
#     #-------------------------------------------------------------------------------------

#     class GridWorldEnv(gym.Env):
#     def __init__(self):
#         super().__init__()
#         self.grid_size = 4
#         self.observation_space = spaces.Discrete(self.grid_size * self.grid_size)
#         self.action_space = spaces.Discrete(4)  # up, down, left, right
#         self.goal = (3, 3)
#         self.state = (0, 0)

#     def reset(self, seed=None, options=None):
#         self.state = (0, 0)
#         return self._to_index(self.state), {}

#     def step(self, action):
#         x, y = self.state

#         if action == 0:   # up
#             x -= 1
#         elif action == 1: # down
#             x += 1
#         elif action == 2: # left
#             y -= 1
#         elif action == 3: # right
#             y += 1

#         x = np.clip(x, 0, self.grid_size - 1)
#         y = np.clip(y, 0, self.grid_size - 1)

#         self.state = (x, y)

#         reward = 1 if self.state == self.goal else 0
#         done = self.state == self.goal

#         return self._to_index(self.state), reward, done, False, {}

#     def _to_index(self, state):
#         return state[0] * self.grid_size + state[1]
    
#     #--------------------------------------------------------------------------------------------

#     class GridObstacleEnv(gym.Env):
#     def __init__(self):
#         super().__init__()
#         self.grid_size = 4
#         self.observation_space = spaces.Discrete(16)
#         self.action_space = spaces.Discrete(4)

#         self.goal = (3, 3)
#         self.obstacle = (1, 1)
#         self.state = (0, 0)

#     def reset(self, seed=None, options=None):
#         self.state = (0, 0)
#         return self._to_index(self.state), {}

#     def step(self, action):
#         x, y = self.state

#         if action == 0: x -= 1
#         elif action == 1: x += 1
#         elif action == 2: y -= 1
#         elif action == 3: y += 1

#         x = np.clip(x, 0, 3)
#         y = np.clip(y, 0, 3)

#         if (x, y) == self.obstacle:
#             reward = -1
#             done = True
#         elif (x, y) == self.goal:
#             reward = 1
#             done = True
#         else:
#             reward = 0
#             done = False

#         self.state = (x, y)
#         return self._to_index(self.state), reward, done, False, {}

#     def _to_index(self, state):
#         return state[0]*4 + state[1]
    
#     #--------------------------------------------------------------------------------------
#     class BanditEnv(gym.Env):
#     def __init__(self):
#         super().__init__()
#         self.observation_space = spaces.Discrete(1)
#         self.action_space = spaces.Discrete(2)

#     def reset(self, seed=None, options=None):
#         return 0, {}

#     def step(self, action):
#         reward = 1 if action == 1 else 0
#         return 0, reward, True, False, {}
#     #-------------------------------------------------------------------------------------------
#     class RandomRewardEnv(gym.Env):
#     def __init__(self):
#         super().__init__()
#         self.observation_space = spaces.Discrete(3)
#         self.action_space = spaces.Discrete(2)
#         self.state = 1

#     def reset(self, seed=None, options=None):
#         self.state = 1
#         return self.state, {}

#     def step(self, action):
#         reward = np.random.choice([0, 1])
#         done = True
#         return self.state, reward, done, False, {}
#--------------------------------------------------------------------------------------------------

#gym_env_names
# Breakout-v0
# Pong-v0
# Seaquest-v0
# Blackjack-v1
# FrozenLake-v1
# FrozenLake8x8-v1
# CliffWalking-v0
# Taxi-v3
# LunarLander-v2
# LunarLanderContinuous-v2
# BipedalWalker-v3
# BipedalWalkerHardcore-v3
# CarRacing-v2
# CartPole-v1
# MountainCar-v0
# MountainCarContinuous-v0
# Pendulum-v1
# Acrobot-v1
