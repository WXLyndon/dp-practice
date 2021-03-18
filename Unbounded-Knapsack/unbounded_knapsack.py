# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack which has a
# capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack. The only difference
# between the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.

# Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items
# which will give us maximum profit such that their cumulative weight is not more than a given number ‘C’. We can
# assume an infinite supply of item quantities; therefore, each item can be selected multiple times.

# Time complexity: O(N * C), space complexity: O(N * C)
def solve_knapsack(profits, weights, capacity):
    n = len(profits)

    # base check
    if capacity <= 0 or n == 0 or n != len(weights):
        return 0

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    for i in range(n):
        for c in range(1, capacity + 1):
            profit1 = 0
            profit2 = 0
            if weights[i] <= c:
                profit1 = profits[i] + dp[i][c - weights[i]]
            if i > 0:
                profit2 = dp[i - 1][c]

            dp[i][c] = max(profit1, profit2)

    return dp[n - 1][capacity]


def main():
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
    print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))


main()
