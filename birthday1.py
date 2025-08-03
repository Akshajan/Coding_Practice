MOD = 10000

def count_arrays(N, K):
    # dp[i][j] = number of arrays of length j ending with number i
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    # Base case: arrays of length 1
    for i in range(1, N + 1):
        dp[i][1] = 1

    for length in range(2, K + 1):  # length from 2 to K
        for i in range(1, N + 1):   # current last number in array
            for j in range(i, N + 1, i):  # all multiples of i (valid next numbers)
                dp[j][length] = (dp[j][length] + dp[i][length - 1]) % MOD

    # Sum all arrays of length K ending with any number from 1 to N
    return sum(dp[i][K] for i in range(1, N + 1)) % MOD

# Example input
N = int(input("Enter N: "))  # Maximum value allowed
K = int(input("Enter K: "))  # Length of the array

print("Total valid arrays:", count_arrays(N, K))
