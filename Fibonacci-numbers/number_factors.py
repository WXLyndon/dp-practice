# Given a number ‘n’, implement a method to count how many possible ways there are to express ‘n’ as the
# sum of 1, 3, or 4.

# EX1: n : 4
#      Number of ways = 4
#      Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4}

# EX2: n : 5
#      Number of ways = 6
#      Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1},
#      {1,4}, {4,1}

def count_ways_mem(n):
    dp = [0 for _ in range(n + 1)]

    return count_ways_recursive(dp, n)


def count_ways_recursive(dp, n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2

    dp[n] = count_ways_recursive(dp, n - 1) + count_ways_recursive(dp, n - 3) + count_ways_recursive(dp, n - 4)

    return dp[n]


def count_way_tab(n):
    dp = [0 for _ in range(n + 1)]

    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

    return dp[n]


def main():
    print(count_ways_mem(4))
    print(count_ways_mem(5))
    print(count_ways_mem(6))
    print(count_way_tab(4))
    print(count_way_tab(5))
    print(count_way_tab(6))


main()
