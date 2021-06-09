# There are n houses built in a line. A thief wants to steal the maximum possible money from
# these houses. The only restriction the thief has is that he can’t steal from two consecutive
# houses, as that would alert the security system. How should the thief maximize his stealing?
# Given a number array representing the wealth of n houses, determine the maximum amount of
# money the thief can steal without alerting the security system.

# EX1: Input: {2, 5, 1, 3, 6, 2, 4}
#      Output: 15
#      Explanation: The thief should steal from houses 5 + 6 + 4

# EX2: Input: {2, 10, 14, 8, 1}
#      Output: 18
#      Explanation: The thief should steal from houses 10 + 8

def find_max_steal_mem(wealth):
    dp = [0 for _ in range(len(wealth))]

    return find_max_steal_recurisve(dp, wealth, 0)


def find_max_steal_recurisve(dp, wealth, currentIndex):
    n = len(wealth)

    if currentIndex >= n:
        return 0

    if dp[currentIndex] == 0:
        # steal from current house and skip next one
        steal = wealth[currentIndex] + \
            find_max_steal_recurisve(dp, wealth, currentIndex + 2)
        # skip current house and steal the next one
        skip = find_max_steal_recurisve(dp, wealth, currentIndex + 1)
        dp[currentIndex] = max(steal, skip)

    return dp[currentIndex]


def find_max_steal_tab(wealth):
    n = len(wealth)

    if n == 0:
        return 0

    dp = [0 for _ in range(n + 1)]  # '+1' to handle the zero house
    dp[0] = 0  # if there are no houses, the thief can't steal anything
    dp[1] = wealth[0]  # only one house, so the thief have to steal from it

    # dp[] has one extra element to handle zero house
    for i in range(1, n):
        dp[i + 1] = max(wealth[i] + dp[i - 1], dp[i])

    return dp[n]


def main():

    print(find_max_steal_mem([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_mem([2, 10, 14, 8, 1]))
    print(find_max_steal_tab([2, 5, 1, 3, 6, 2, 4]))
    print(find_max_steal_tab([2, 10, 14, 8, 1]))


main()
