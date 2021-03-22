# Given a number array to represent different coin denominations and a total amount ‘T’, we need to find
# the minimum number of coins needed to make change for ‘T’. We can assume an infinite supply of coins,
# therefore, each coin can be chosen multiple times.

# EX 1: Denominations: {1,2,3}
#       Total amount: 5
#       Output: 2
#       Explanation: We need minimum of two coins {2,3} to make a total of '5'
#
# EX 2: Denominations: {1,2,3}
#       Total amount: 11
#       Output: 4
#       Explanation: We need minimum four coins {2,3,3,3} to make a total of '11'


def count_change_mem(denominations, total):
    n = len(denominations)
    dp = [[-1 for _ in range(total + 1)] for _ in range(n)]
    result = count_change_recursive(dp, denominations, total, 0)
    return -1 if result == float("inf") else result


def count_change_recursive(dp, denominations, total, currentIndex):
    n = len(denominations)

    if total == 0:
        return 0

    if n == 0 or currentIndex >= n:
        return float("inf")

    # Check if a similar sub-problem is already solved
    if dp[currentIndex][total] == -1:

        count1 = float("inf")
        # include the ith coin
        if denominations[currentIndex] <= total:
            res = count_change_recursive(dp, denominations, total - denominations[currentIndex], currentIndex)
            if res != float("inf"):
                count1 = res + 1

        # exclude the ith coins
        count2 = count_change_recursive(dp, denominations, total, currentIndex + 1)

        dp[currentIndex][total] = min(count1, count2)

    return dp[currentIndex][total]


def count_change_tab(denominations, total):
    n = len(denominations)

    if n == 0 or total == 0:
        return 0

    dp = [[float("inf") for _ in range(total + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for j in range(1, total + 1):

            if i > 0:
                dp[i][j] = dp[i - 1][j]

            if denominations[i] <= j:
                if dp[i][j - denominations[i]] != float("inf"):
                    dp[i][j] = min(dp[i][j], dp[i][j - denominations[i]] + 1)

    return -1 if dp[n - 1][total] == float("inf") else dp[n - 1][total]


def main():
    print(count_change_mem([1, 2, 3], 5))
    print(count_change_mem([1, 2, 3], 11))
    print(count_change_mem([1, 2, 3], 7))
    print(count_change_mem([3, 5], 7))
    print(count_change_tab([1, 2, 3], 5))
    print(count_change_tab([1, 2, 3], 11))
    print(count_change_tab([1, 2, 3], 7))
    print(count_change_tab([3, 5], 7))


main()
