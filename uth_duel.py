import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# -------------------------
# Environment
# -------------------------
class LineWorld:
    def reset(self):
        self.state = 2
        return self.state

    def step(self, action):
        self.state += -1 if action == 0 else 1

        if self.state == 4:
            return self.state, 1.0, True   # goal
        if self.state == 0:
            return self.state, 0.0, True   # bad end

        return self.state, 0.0, False


# -------------------------
# One-hot encoding
# -------------------------
def one_hot(state):
    x = np.zeros(5)
    x[state] = 1
    return torch.tensor(x, dtype=torch.float32)


# -------------------------
# Dueling DQN Model
# -------------------------
class DuelingDQN(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(5, 16)
        self.value = nn.Linear(16, 1)
        self.advantage = nn.Linear(16, 2)

    def forward(self, x):
        x = torch.relu(self.fc(x))
        V = self.value(x)
        A = self.advantage(x)
        return V + (A - A.mean())


# -------------------------
# Setup
# -------------------------
env = LineWorld()
net = DuelingDQN()
target_net = DuelingDQN()
target_net.load_state_dict(net.state_dict())

optimizer = optim.Adam(net.parameters(), lr=0.01)

buffer = []
gamma = 0.9
epsilon = 0.2
batch_size = 16


# -------------------------
# Training
# -------------------------
for episode in range(300):
    state = env.reset()
    done = False
    total_reward = 0

    while not done:
        s = one_hot(state)

        # Epsilon-greedy action
        if random.random() < epsilon:
            action = random.randint(0, 1)
        else:
            action = torch.argmax(net(s)).item()

        next_state, reward, done = env.step(action)
        total_reward += reward

        buffer.append((state, action, reward, next_state, done))

        # Train only if enough samples
        if len(buffer) >= batch_size:
            batch = random.sample(buffer, batch_size)

            loss = 0
            for s, a, r, s_next, d in batch:
                s_t = one_hot(s)
                s_next_t = one_hot(s_next)

                q_sa = net(s_t)[a]

                with torch.no_grad():
                    if d:
                        y = r
                    else:
                        y = r + gamma * torch.max(target_net(s_next_t))

                loss += (y - q_sa) ** 2

            loss = loss / batch_size

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        state = next_state

    # Update target network every 20 episodes
    if episode % 20 == 0:
        target_net.load_state_dict(net.state_dict())

    # Print progress
    if episode % 50 == 0:
        print(f"Episode {episode} | Total Reward: {total_reward}")


print("\nTraining completed!\n")


# -------------------------
# Testing / Results
# -------------------------
print("Learned Q-values:\n")
for s in range(5):
    q = net(one_hot(s)).detach().numpy()
    print(f"State {s} → Left: {q[0]:.3f}, Right: {q[1]:.3f}")


print("\nPolicy (Best Action):")
for s in range(5):
    action = torch.argmax(net(one_hot(s))).item()
    direction = "Left" if action == 0 else "Right"
    print(f"State {s} → {direction}")
