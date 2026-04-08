#gen_iter
# gamma = 0.9
# states = ["Idle", "Working"]
# actions = ["Start", "Wait"]
# policy = {s: "Start" for s in states}
# V = {s: 0 for s in states}
# def reward(s, a):
#     if a == "Start":
#         return 8
#     return -1
# def next_state(s, a):
#     if a == "Start":
#         return "Working"
#     return "Idle"
# for _ in range(20):
#     # Policy Evaluation
#     for _ in range(10):
#         for s in states:
#             a = policy[s]
#             V[s] = reward(s, a) + gamma * V[next_state(s, a)]
#     # Policy Improvement
#     stable = True
#     for s in states:
#         old = policy[s]
#         values = {}
#         for a in actions:
#             values[a] = reward(s, a) + gamma * V[next_state(s, a)]
#         policy[s] = max(values, key=values.get)
#         if old != policy[s]:
#             stable = False
#     if stable:
#         break
# print("Optimal Policy:", policy)
# print("State Values:", V)
#-----------------------------------------------------------------------------------------

#stochstic_transitions

# gamma = 0.9
# states = ["Idle", "Working"]
# actions = ["Start", "Wait"]
# policy = {s: "Start" for s in states}
# V = {s: 0 for s in states}
# def reward(s, a):
#     if a == "Start":
#         return 8
#     return -1
# # STOCHASTIC TRANSITIONS
# def transitions(s, a):
#     if a == "Start":
#         return [("Working", 0.8), ("Idle", 0.2)]
#     else:
#         return [("Idle", 1.0)]
# for _ in range(20):
#     # Policy Evaluation
#     for _ in range(10):
#         for s in states:
#             a = policy[s]
#             V[s] = sum(p * (reward(s, a) + gamma * V[s_next])
#                        for (s_next, p) in transitions(s, a))
#     # Policy Improvement
#     stable = True
#     for s in states:
#         old = policy[s]
#         values = {}
#         for a in actions:
#             values[a] = sum(p * (reward(s, a) + gamma * V[s_next])
#                             for (s_next, p) in transitions(s, a))
#         policy[s] = max(values, key=values.get)
#         if old != policy[s]:
#             stable = False
#     if stable:
#         break
# print("Optimal Policy:", policy)
# print("V:", V)

#--------------------------------------------------------------------------------------

#terminal

# gamma = 0.9
# states = ["Start", "Middle", "Goal"]
# actions = ["Go", "Wait"]
# policy = {s: "Go" for s in states}
# V = {s: 0 for s in states}
# def reward(s, a):
#     return 10 if s == "Middle" and a == "Go" else -1
# def next_state(s, a):
#     if s == "Start":
#         return "Middle"
#     elif s == "Middle":
#         return "Goal"
#     return "Goal"
# for _ in range(20):
#     # Policy Evaluation
#     for _ in range(10):
#         for s in states:
#             # TERMINAL CONDITION
#             if s == "Goal":
#                 V[s] = 0
#                 continue
#             a = policy[s]
#             s_next = next_state(s, a)
#             V[s] = reward(s, a) + gamma * V[s_next]
#     # Policy Improvement
#     stable = True
#     for s in states:
#         if s == "Goal":
#             continue
#         old = policy[s]
#         values = {}
#         for a in actions:
#             s_next = next_state(s, a)
#             values[a] = reward(s, a) + gamma * V[s_next]
#         policy[s] = max(values, key=values.get)
#         if old != policy[s]:
#             stable = False
#     if stable:
#         break
# print("Optimal Policy:", policy)

#--------------------------------------------------------------------------------------------------------------

#reward only when reaching goal

# gamma = 0.9
# states = ["A", "B", "Goal"]
# actions = ["Move"]
# policy = {s: "Move" for s in states}
# V = {s: 0 for s in states}
# def next_state(s, a):
#     if s == "A":
#         return "B"
#     elif s == "B":
#         return "Goal"
#     return "Goal"
# def reward(s, a, s_next):
#     return 10 if s_next == "Goal" else -1
# for _ in range(20):
#     # Policy Evaluation
#     for _ in range(10):
#         for s in states:
#             if s == "Goal":
#                 V[s] = 0
#                 continue
#             a = policy[s]
#             s_next = next_state(s, a)
#             V[s] = reward(s, a, s_next) + gamma * V[s_next]
#     # Policy Improvement
#     stable = True
#     for s in states:
#         if s == "Goal":
#             continue
#         old = policy[s]
#         values = {}
#         for a in actions:
#             s_next = next_state(s, a)
#             values[a] = reward(s, a, s_next) + gamma * V[s_next]
#         policy[s] = max(values, key=values.get)
#         if old != policy[s]:
#             stable = False
#     if stable:
#         break
# print("Optimal Policy:", policy)

#---------------------------------------------------------------------------------------------

#grid

# gamma = 0.9

# grid_size = 3
# states = [(i, j) for i in range(grid_size) for j in range(grid_size)]
# actions = ["up", "down", "left", "right"]

# goal = (2, 2)

# policy = {s: "up" for s in states}
# V = {s: 0 for s in states}

# def next_state(s, a):
#     i, j = s
#     if a == "up": i = max(i-1, 0)
#     if a == "down": i = min(i+1, grid_size-1)
#     if a == "left": j = max(j-1, 0)
#     if a == "right": j = min(j+1, grid_size-1)
#     return (i, j)

# def reward(s, a):
#     return 10 if s == goal else -1

# for _ in range(20):

#     for _ in range(10):
#         for s in states:

#             if s == goal:
#                 V[s] = 0
#                 continue

#             a = policy[s]
#             s_next = next_state(s, a)

#             V[s] = reward(s, a) + gamma * V[s_next]

#     stable = True
#     for s in states:

#         if s == goal:
#             continue

#         old = policy[s]

#         values = {}
#         for a in actions:
#             s_next = next_state(s, a)
#             values[a] = reward(s, a) + gamma * V[s_next]

#         policy[s] = max(values, key=values.get)

#         if old != policy[s]:
#             stable = False

#     if stable:
#         break
# print("Optimal Policy:", policy)

#------------------------------------------------------------------------------------------
#multiple action rewars
# gamma = 0.9

# states = ["S"]
# actions = ["A1", "A2", "A3"]

# policy = {"S": "A1"}
# V = {"S": 0}

# def reward(s, a):
#     if a == "A1": return 5
#     elif a == "A2": return 10
#     else: return -2

# def next_state(s, a):
#     return "S"

# for _ in range(10):

#     # Policy Evaluation
#     for _ in range(5):
#         V["S"] = reward("S", policy["S"]) + gamma * V["S"]

#     # Policy Improvement
#     values = {}
#     for a in actions:
#         values[a] = reward("S", a) + gamma * V["S"]

#     policy["S"] = max(values, key=values.get)

# print("Optimal Policy:", policy)

#----------------------------------------------------------------------------------------------

#uth

# gamma = 0.9

# states = ["Idle", "Working"]
# actions = ["Start", "Wait"]

# # Initialize policy randomly
# policy = {
#     "Idle": "Wait",
#     "Working": "Start"
# }

# V = {state: 0 for state in states}

# def reward(state, action):
#     if action == "Start":
#         return 8
#     else:
#         return -1

# def next_state(state, action):
#     if action == "Start":
#         return "Working"
#     return "Idle"

# # Policy Iteration
# for iteration in range(10):

#     # Policy Evaluation
#     for _ in range(10):
#         for s in states:
#             a = policy[s]
#             V[s] = reward(s, a) + gamma * V[next_state(s, a)]

#     # Policy Improvement
#     policy_stable = True
#     for s in states:
#         old_action = policy[s]
#         action_values = {}

#         for a in actions:
#             action_values[a] = reward(s, a) + gamma * V[next_state(s, a)]

#         policy[s] = max(action_values, key=action_values.get)

#         if old_action != policy[s]:
#             policy_stable = False

#     print(f"Iteration {iteration+1}: Policy = {policy}, V = {V}")

#     if policy_stable:
#         break
