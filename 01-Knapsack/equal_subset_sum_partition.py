# Given a set of positive numbers, find if we can partition it into two subsets such that the sum of
# elements in both the subsets is equal.

# EX1: Input: {1, 2, 3, 4}
#      Output: True
#      Explanation: The given set can be partitioned into two subsets with equal sum: {1, 4} & {2, 3}
# EX2: Input: {1, 1, 3, 4, 7}
#      Output: True
#      Explanation: The given set can be partitioned into two subsets with equal sum: {1, 3, 4} & {1, 7}
# EX3: Input: {2, 3, 4, 6}
#      Output: False
#      Explanation: The given set cannot be partitioned into two subsets with equal sum.

# Time complexity: O(n * s), space complexity: O(n * s)
def can_partition(num):
    n = len(num)
    s = sum(num)

    # The subset cannot be divide into two subsets with each sum of s/2
    if s % 2 != 0:
        return False

    s = s // 2

    dp = [[False for y in range(s + 1)] for x in range(n)]

    for i in range(n):
        dp[i][0] = True

    for i in range(1, s + 1):
        dp[0][i] = True if num[0] == i else False

    for i in range(1, n):
        for j in range(1, s + 1):

            if dp[i - 1][j]:  # if we can get the sum without i-th number
                dp[i][j] = True
            elif num[i] <= j:  # check if we can find a subset to get the remaining sum
                dp[i][j] = dp[i - 1][j - num[i]]

    return dp[n - 1][s]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))


main()
