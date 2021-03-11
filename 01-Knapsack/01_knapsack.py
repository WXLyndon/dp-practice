# Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack
# that has a capacity ‘C’. The goal is to get the maximum profit from the items in the knapsack.
# Each item can only be selected once, as we don’t have multiple quantities of any item.

# Time complexity: O(N * C), space complexity: O(N * C)
def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    # basic check
    if capacity <= 0 or n == 0 or n != len(weights):
        return 0

    dp = [[0 for y in range(capacity+1)] for x in range(n)]

    # if we only have one item, then we will take it if its weight is not more than the capacity
    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(1, n):
        for c in range(1, capacity + 1):
            selectedProfit = 0
            excludedProfit = 0

            # if we choose the i-th item
            if weights[i] <= c:
                selectedProfit = profits[i] + dp[i - 1][c - weights[i]]

            # if we choose to exclue the i-th item
            excludedProfit = dp[i-1][c]

            # take the maximum
            dp[i][c] = max(selectedProfit, excludedProfit)

    print_selected_items(dp, profits, weights, capacity)

    # maximum profit will be at the bottome-right corner
    return dp[n-1][capacity]


def print_selected_items(dp, profits, weights, capacity):
    print("Selected weights are:", end='')
    n = len(weights)
    maxProfit = dp[n - 1][capacity]

    for i in range(n - 1, 0, -1):
        if maxProfit != dp[i - 1][capacity]:
            print(str(weights[i]) + " ", end='')
            maxProfit -= profits[i]
            capacity -= weights[i]

    if maxProfit != 0:
        print(str(weights[0]) + " ", end='')
    print()


# Time complexity: O(N * C), space complexity: O(C) (We can just use one previous row)
def solve_knapsack_opt(profits, weights, capacity):

    n = len(profits)
    if capacity <= 0 or n == 0 or n != len(weights):
        return 0

    dp = [[0 for y in range(capacity + 1)] for x in range(2)]

    for c in range(capacity + 1):
        if weights[0] <= c:
            dp[0][c] = profits[0]

    for i in range(n):
        for c in range(capacity + 1):
            selectedProfit = 0
            excludedProfit = 0

            if weights[i] <= c:
                selectedProfit = profits[i] + dp[(i % 2) - 1][c - weights[i]]

            excludedProfit = dp[(i % 2) - 1][c]

            dp[i % 2][c] = max(selectedProfit, excludedProfit)

    return dp[(n - 1) % 2][capacity]


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack_opt([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve_knapsack_opt([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve_knapsack_opt([1, 6, 10, 16], [1, 2, 3, 5], 7))


main()
