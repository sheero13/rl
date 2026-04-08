import random

# ----- 1. Define Environment -----
states = ["S0", "S1", "S2", "S3", "S4"]   # generic states
actions = ["Left", "Right"]               # generic actions
goal_state = "S4"                         # goal if any
step_cost = -1                             # per step cost
goal_reward = 10                            # reward at goal
num_episodes = 100
gamma = 0.9                                # discount factor
alpha = 0.1                                # learning rate for TD
epsilon = 0.1                              # exploration for ε-greedy

# ----- 2. Select RL Method -----
method = "SARSA"  # choose: "MC_V", "MC_Q", "SARSA", "QL"

# ----- 3. Initialize Values -----
V = {s: 0 for s in states}                    # for MC_V
returns_V = {s: [] for s in states}

Q = {s: {a: 0 for a in actions} for s in states}    # for MC_Q, SARSA, QL
returns_Q = {s: {a: [] for a in actions} for s in states}

# ----- 4. Helper: ε-greedy -----
def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)
    return max(Q[state], key=Q[state].get)

# ----- 5. Simulation -----
for episode in range(num_episodes):
    if method == "MC_V":
        # Monte Carlo First-Visit V(s)
        state = random.choice(states)
        # Example: simple reward table
        reward_table = {s: step_cost for s in states}
        reward_table[goal_state] = goal_reward
        G = reward_table[state]
        returns_V[state].append(G)
        V[state] = sum(returns_V[state]) / len(returns_V[state])

    elif method == "MC_Q":
        # Monte Carlo Control Q(s,a) with ε-greedy
        state = random.choice(states)
        action = choose_action(state) if random.random() > epsilon else random.choice(actions)
        # Example reward mapping
        reward = goal_reward if state == goal_state else step_cost
        returns_Q[state][action].append(reward)
        Q[state][action] = sum(returns_Q[state][action]) / len(returns_Q[state][action])

    elif method in ["SARSA", "QL"]:
        # TD Control (SARSA = on-policy, QL = off-policy)
        state = states[0]  # start state
        action = choose_action(state)
        while state != goal_state:
            # Example transition: move "Right" always
            next_state = states[min(states.index(state)+1, len(states)-1)]
            reward = goal_reward if next_state == goal_state else step_cost
            next_action = choose_action(next_state)
            
            td_target = reward + gamma * (
                Q[next_state][next_action] if method=="SARSA"
                else max(Q[next_state].values())   # Q-learning off-policy
            )
            td_error = td_target - Q[state][action]
            Q[state][action] += alpha * td_error
            
            # Print TD error step (optional)
            # print(f"State:{state} Action:{action} TD_error:{td_error:.2f}")

            state, action = next_state, next_action

# ----- 6. Print Results -----
if method == "MC_V":
    print("Estimated V(s):")
    print(V)
else:
    print(f"Estimated Q(s,a) using {method}:")
    for s in Q:
        print(f"State {s}: {Q[s]}")
