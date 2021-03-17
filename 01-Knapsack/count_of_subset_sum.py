# Given a set of positive numbers, find the total number of subsets whose sum is equal to a given number ‘S’.

# EX 1: Input: {1, 1, 2, 3}, S=4
#       Output: 3
#       The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
#       Note that we have two similar sets {1, 3}, because we have two '1' in our input.
# EX2:  Input: {1, 2, 7, 1, 5}, S=9
#       Output: 3
#       The given set has '3' subsets whose sum is '9': {2, 7}, {1, 7, 1}, {1, 2, 1, 5}

# Time complexity: O(n * sum), space complexity: O(n * sum)
def count_subsets(num, sum):
    n = len(num)

    dp = [[0 for y in range(sum + 1)] for y in range(n)]

    # We always have an empty set for zero sum
    for i in range(n):
        dp[i][0] = 1

    # With only one number, we can form a subset only when the required sum is equal to its value
    for s in range(1, sum + 1):
        if s == num[0]:
            dp[0][s] = 1

    for i in range(1, n):
        for s in range(1, sum + 1):

            # exclude the ith number
            dp[i][s] = dp[i - 1][s]

            # include the number, if it does not exceed the sum
            if num[i] <= s:
                dp[i][s] += dp[i - 1][s - num[i]]

    return dp[n - 1][sum]


# Time complexity: O(n * sum), space complexity: O(sum)
def count_subsets_opt1(num, sum):
    n = len(num)

    dp = [[0 for y in range(sum + 1)] for x in range(2)]

    # We always have an empty set for zero sum
    for i in range(n):
        dp[i % 2][0] = 1

    # With only one number, we can form a subset only when the required sum is equal to its value
    for s in range(1, sum + 1):
        if s == num[0]:
            dp[0][s] = 1

    for i in range(1, n):
        for s in range(1, sum + 1):

            # exclude the ith number
            dp[i % 2][s] = dp[i % 2 - 1][s]

            # include the number, if it does not exceed the sum
            if num[i] <= s:
                dp[i % 2][s] += dp[i % 2 - 1][s - num[i]]

    return dp[(n - 1) % 2][sum]


# Time complexity: O(n * sum), space complexity: O(sum)
def count_subsets_opt2(num, sum):
    n = len(num)

    dp = [0 for _ in range(sum + 1)]

    dp[0] = 1

    for s in range(1, sum + 1):
        if s == num[0]:
            dp[s] = 1

    for i in range(1, n):
        for s in range(sum, -1, -1):
            if num[i] <= s:
                dp[s] += dp[s - num[i]]

    return dp[sum]


def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))
    print("Total number of subsets " +
          str(count_subsets_opt1([1, 1, 2, 3], 4)))
    print("Total number of subsets: " +
          str(count_subsets_opt1([1, 2, 7, 1, 5], 9)))
    print("Total number of subsets " +
          str(count_subsets_opt2([1, 1, 2, 3], 4)))
    print("Total number of subsets: " +
          str(count_subsets_opt2([1, 2, 7, 1, 5], 9)))


main()
