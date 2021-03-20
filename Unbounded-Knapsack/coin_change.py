# Given an infinite supply of ‘n’ coin denominations and a total money amount, we are asked to find the
# total number of distinct ways to make up that amount.

# Example:
# Denominations: {1,2,3}
# Total amount: 5
# Output: 5
# Explanation: There are five ways to make the change for '5', here are those ways:
#   1. {1,1,1,1,1}
#   2. {1,1,1,2}
#   3. {1,2,2}
#   4. {1,1,3}
#   5. {2,3}

def count_change_mem(denominations, total):
    dp = [[-1 for _ in range(total + 1)] for _ in range(len(denominations))]
    return count_change_recursive(dp, denominations, total, 0)


def count_change_recursive(dp, denominations, total, currentIndex):
    # base cases
    if total == 0:
        return 1

    n = len(denominations)
    if n == 0 or currentIndex >= n:
        return 0

    if dp[currentIndex][total] != -1:
        return dp[currentIndex][total]

    sum1 = 0
    if denominations[currentIndex] <= total:
        sum1 = count_change_recursive(dp, denominations, total - denominations[currentIndex], currentIndex)

    sum2 = count_change_recursive(dp, denominations, total, currentIndex + 1)

    dp[currentIndex][total] = sum1 + sum2

    return dp[currentIndex][total]


# Time complexity: O(len(denominations) * len(total)), space complexity: O(len(denominations) * len(total))
def count_change_tab(denominations, total):
    n = len(denominations)

    dp = [[0 for _ in range(total + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for t in range(1, total + 1):

            if i > 0:
                dp[i][t] = dp[i - 1][t]

            if denominations[i] <= t:
                dp[i][t] += dp[i][t - denominations[i]]

    return dp[n - 1][total]


def main():
    print(count_change_mem([1, 2, 3], 5))
    print(count_change_tab([1, 2, 3], 5))


main()
