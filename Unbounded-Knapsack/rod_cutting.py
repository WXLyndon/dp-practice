# Given a rod of length ‘n’, we are asked to cut the rod and sell the pieces in a way that will maximize the
# profit. We are also given the price of every piece of length ‘i’ where ‘1 <= i <= n’.

# Example:
# Lengths: [1, 2, 3, 4, 5]
# Prices: [2, 6, 7, 10, 13]
# Rod Length: 5
# Max profit: 14

# Time complexity: O(n * size), space complexity: O(n * size)
def solve_rod_cutting(lengths, prices, n):
    size = len(lengths)

    if size <= 0 or size != len(prices) or n == 0:
        return 0

    dp = [[0 for _ in range(n + 1)] for _ in range(size)]

    for i in range(size):
        for length in range(1, n + 1):
            price1 = 0
            price2 = 0

            # cut i-th length rod
            if lengths[i] <= length:
                price1 = prices[i] + dp[i][length - lengths[i]]

            # exclude the i-th length rod
            if i > 0:
                price2 = dp[i - 1][length]
            dp[i][length] = max(price1, price2)

    return dp[size - 1][n]


def main():
    print(solve_rod_cutting([1, 2, 3, 4, 5], [2, 6, 7, 10, 13], 5))


main()
