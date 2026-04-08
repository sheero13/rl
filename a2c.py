# # Filename: a2c_cartpole.py

# import gymnasium as gym 
# import torch
# import torch.nn as nn
# import torch.optim as optim

# # -------- ENVIRONMENT --------
# env = gym.make("CartPole-v1")

# state_dim = env.observation_space.shape[0]
# action_dim = env.action_space.n

# # -------- ACTOR-CRITIC NETWORK --------
# class ActorCritic(nn.Module):
#     def __init__(self):
#         super().__init__()

#         self.shared = nn.Sequential(
#             nn.Linear(state_dim, 64),
#             nn.ReLU()
#         )

#         # Actor (policy)
#         self.actor = nn.Sequential(
#             nn.Linear(64, action_dim),
#             nn.Softmax(dim=-1)
#         )

#         # Critic (value function)
#         self.critic = nn.Linear(64, 1)

#     def forward(self, x):
#         x = self.shared(x)
#         return self.actor(x), self.critic(x)

# # -------- INITIALIZE --------
# model = ActorCritic()
# optimizer = optim.Adam(model.parameters(), lr=0.001)
# gamma = 0.99

# # -------- TRAINING --------
# num_episodes = 300

# for episode in range(num_episodes):
#     state, _ = env.reset()
#     done = False
#     total_reward = 0

#     while not done:
#         state_tensor = torch.tensor(state, dtype=torch.float32)

#         # Get policy and value
#         probs, value = model(state_tensor)
#         dist = torch.distributions.Categorical(probs)

#         action = dist.sample()
#         log_prob = dist.log_prob(action)

#         next_state, reward, done, truncated, _ = env.step(action.item())
#         total_reward += reward

#         next_state_tensor = torch.tensor(next_state, dtype=torch.float32)
#         _, next_value = model(next_state_tensor)

#         # -------- COMPUTE TARGET --------
#         target = reward + gamma * next_value * (1 - int(done))

#         # -------- ADVANTAGE --------
#         advantage = target - value

#         # -------- LOSSES --------
#         actor_loss = -log_prob * advantage.detach()
#         critic_loss = advantage.pow(2)

#         loss = actor_loss + critic_loss

#         # -------- UPDATE --------
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()

#         state = next_state

#         if truncated:
#             break

#     # -------- PRINT --------
#     if (episode + 1) % 20 == 0:
#         print(f"Episode {episode+1}, Reward: {total_reward}")

# print("\nTraining completed!")

# # -------- TEST --------
# state, _ = env.reset()
# done = False
# total_reward = 0

# while not done:
#     state_tensor = torch.tensor(state, dtype=torch.float32)
#     probs, _ = model(state_tensor)

#     action = torch.argmax(probs).item()
#     state, reward, done, truncated, _ = env.step(action)

#     total_reward += reward

#     if truncated:
#         break

# print(f"\nTest Reward: {total_reward}")

# env.close()
