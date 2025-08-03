#  You're given a row of binary cells, like this: 1 0 1 1 0
# 🔸 Each cell looks at its neighbors:
# Left neighbor (the cell before it)
# Right neighbor (the cell after it)

# 🔸 Update rule for each day:
# For every cell:
# If the left and right neighbors are the same (both 0 or both 1), the cell becomes 0
# If the left and right neighbors are different (one is 0, the other is 1), the cell becomes 1

# 🔸 Special Rule for Edges:
# The first cell has no left neighbor → treat it as 0
# The last cell has no right neighbor → treat it as 0

# 🔁 Repeat this process for D days.

# Input format
# N       → (number of cells)
# S       → (a string of N characters, each 0 or 1, representing the initial state)
# D       → (number of days to simulate)

def simulate_cells(N, S, D):
    state = [int(x) for x in S] # Convert string to list of ints

    for _ in range(D):
        new_state = []
        for i in range(N):
            left = state[i - 1] if i > 0 else 0
            right = state[i + 1] if i < N - 1 else 0
            new_state.append(0 if left == right else 1)
        state = new_state

    return ''.join(map(str, state))

N = int(input("Enter the number of cells: "))
S = input("Enter the binary string: ")
D = int(input("Enter the number of days to stimulate: "))

final_state = simulate_cells(N, S, D)
print("Final state after", D, "days:", final_state)
