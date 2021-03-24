# Given a stair with ‘n’ steps, implement a method to count how many possible ways are there to reach
# the top of the staircase, given that, at every step you can either take 1 step, 2 steps, or 3 steps.

# EX1: Number of stairs (n) : 3
#      Number of ways = 4
#      Explanation: Following are the four ways we can climb : {1,1,1}, {1,2}, {2,1}, {3}

# EX2: Number of stairs (n) : 4
#      Number of ways = 7
#      Explanation: Following are the seven ways we can climb : {1,1,1,1}, {1,1,2}, {1,2,1}, {2,1,1},
#      {2,2}, {1,3}, {3,1}

def count_ways_mem(n):
    dp = [0 for x in range(n + 1)]
    return count_ways_recursive(dp, n)


# Time & Space complexity: O(N)
def count_ways_recursive(dp, n):
    if n == 0:
        return 1  # base case, we don't need to take any step, so there is only one way

    if n == 1:
        return 1  # we can take one step to reach the end, and that is the only way

    if n == 2:
        return 2  # we can take one step twice or jump two steps to reach at the top

    if dp[n] == 0:
        # if we take 1 step, we are left with 'n-1' steps;
        take1Step = count_ways_recursive(dp, n - 1)
        # similarly, if we took 2 steps, we are left with 'n-2' steps;
        take2Step = count_ways_recursive(dp, n - 2)
        # if we took 3 steps, we are left with 'n-3' steps;
        take3Step = count_ways_recursive(dp, n - 3)

        dp[n] = take1Step + take2Step + take3Step

    return dp[n]


# Time & Space complexity: O(N)
def count_ways_tab(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]


# Time complexity: O(N), Space complexity: O(1)
def count_ways_tab_opt(n):
    if n < 2:
        return 1
    if n == 2:
        return 2
    s1 = 1
    s2 = 1
    s3 = 2
    for i in range(3, n + 1):
        temp = s1 + s2 + s3
        s1 = s2
        s2 = s3
        s3 = temp

    return s3


def main():
    print(count_ways_mem(3))
    print(count_ways_mem(4))
    print(count_ways_mem(5))
    print(count_ways_tab(3))
    print(count_ways_tab(4))
    print(count_ways_tab(5))
    print(count_ways_tab_opt(3))
    print(count_ways_tab_opt(4))
    print(count_ways_tab_opt(5))


main()
