# # Filename: vanilla_policy_gradient_cartpole.py

# import gymnasium as gym
# import torch
# import torch.nn as nn
# import torch.optim as optim

# # -------- ENVIRONMENT --------
# env = gym.make("CartPole-v1")

# state_dim = env.observation_space.shape[0]
# action_dim = env.action_space.n

# # -------- POLICY NETWORK --------
# class PolicyNetwork(nn.Module):
#     def __init__(self):
#         super().__init__()

#         self.model = nn.Sequential(
#             nn.Linear(state_dim, 64),
#             nn.ReLU(),
#             nn.Linear(64, action_dim),
#             nn.Softmax(dim=-1)
#         )

#     def forward(self, x):
#         return self.model(x)

# # -------- INITIALIZE --------
# policy = PolicyNetwork()
# optimizer = optim.Adam(policy.parameters(), lr=0.01)
# gamma = 0.99

# # -------- TRAINING --------
# num_episodes = 300

# for episode in range(num_episodes):
#     state, _ = env.reset()

#     log_probs = []
#     rewards = []

#     done = False

#     while not done:
#         state_tensor = torch.tensor(state, dtype=torch.float32)

#         probs = policy(state_tensor)
#         dist = torch.distributions.Categorical(probs)

#         action = dist.sample()
#         log_prob = dist.log_prob(action)

#         next_state, reward, done, truncated, _ = env.step(action.item())

#         log_probs.append(log_prob)
#         rewards.append(reward)

#         state = next_state

#         if truncated:
#             break

#     # -------- COMPUTE RETURNS --------
#     returns = []
#     G = 0

#     for r in reversed(rewards):
#         G = r + gamma * G
#         returns.insert(0, G)

#     returns = torch.tensor(returns)

#     # Normalize (important for stability)
#     returns = (returns - returns.mean()) / (returns.std() + 1e-8)

#     # -------- LOSS --------
#     loss = 0
#     for log_prob, G in zip(log_probs, returns):
#         loss += -log_prob * G

#     # -------- UPDATE --------
#     optimizer.zero_grad()
#     loss.backward()
#     optimizer.step()

#     # -------- PRINT --------
#     if (episode + 1) % 20 == 0:
#         print(f"Episode {episode+1}, Total Reward: {sum(rewards)}")

# print("\nTraining completed!")

# # -------- TEST --------
# state, _ = env.reset()
# done = False
# total_reward = 0

# while not done:
#     state_tensor = torch.tensor(state, dtype=torch.float32)
#     probs = policy(state_tensor)
#     action = torch.argmax(probs).item()

#     state, reward, done, truncated, _ = env.step(action)
#     total_reward += reward

#     if truncated:
#         break

# print(f"\nTest Reward: {total_reward}")

# env.close()
