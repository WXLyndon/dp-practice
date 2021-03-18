# Given a set of positive numbers (non zero) and a target sum ‘S’. Each number should be
# assigned either a ‘+’ or ‘-’ sign. We need to find out total ways to assign symbols to
# make the sum of numbers equal to target ‘S’.

# EX 1: Input: {1, 1, 2, 3}, S=1
#       Output: 3
#       Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
# EX 2: Input: {1, 2, 7, 1}, S=9
#       Output: 2
#       Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}

# Idea: We actually want to find two subsets(s1, s2) that their difference is equal to S (sum(s1) - sum(s2) = S).
# And we know that sum(s1) + sum(s2) = sum(num), so we add these two equations then we can get a new equation:
# sum(s1) + sum(s2) + sum(s1) - sum(s2)  = sum(num) + S, to simplify it we could get： 2sum(s1) = sum(num) + S =>
# sum(s1) = (sum(num) + S) / 2. Therefore, we only need to find the count of subsets of their sum is equal to
# (sum(num) + S) / 2.

def find_target_subsets(num, s):
    if any(i < 1 for i in num):
        return -1  # invalid input

    total = sum(num)

    if total < s or (s + total) % 2 != 0:
        return 0

    # return count_subsets(num, (s + total) // 2)
    return count_subsets_opt(num, (s + total) // 2)


# this function is exactly similar to 'Count of Subset Sum' problem.
def count_subsets(num, s):
    n = len(num)

    dp = [[0 for y in range(s + 1)] for x in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(1, s + 1):
        dp[0][i] = 1 if i == num[0] else 0

    for i in range(1, n):
        for j in range(1, s + 1):

            # exclude the ith number
            dp[i][j] = dp[i - 1][j]

            # include the ith number
            if num[i] <= j:
                dp[i][j] += dp[i - 1][j - num[i]]

    return dp[n - 1][s]


# using only a single array
def count_subsets_opt(num, s):
    n = len(num)

    dp = [0 for _ in range(s + 1)]

    dp[0] = 1

    for i in range(1, s + 1):
        dp[i] = 1 if i == num[0] else 0

    for i in range(1, n):
        for j in range(s, -1, -1):

            if num[i] <= j:
                dp[j] += dp[j - num[i]]

    return dp[s]


def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))


main()
