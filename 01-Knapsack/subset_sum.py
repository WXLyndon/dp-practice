# Given a set of positive numbers, determine if there exists a subset whose sum is equal to a given
# number ‘S’.

# EX 1: Input: {1, 2, 3, 7}, S=6
#       Output: True
#       The given set has a subset whose sum is '6': {1, 2, 3}
# EX 2: Input: {1, 2, 7, 1, 5}, S=10
#       Output: True
#       The given set has a subset whose sum is '10': {1, 2, 7}
# EX 3: Input: {1, 3, 4, 8}, S=6
#       Output: False
#       The given set does not have any subset whose sum is equal to '6'.

# Time complexity: O(n * sum), space complexity: O(n * sum)
def can_partition(num, sum):
    n = len(num)

    dp = [[False for y in range(sum + 1)] for x in range(n)]

    # We always can get a 0 sum subset(empty set)
    for i in range(n):
        dp[i][0] = True

    for s in range(sum + 1):
        dp[0][s] = True if num[0] == s else False

    for i in range(1, n):
        for s in range(1, sum + 1):
            # if we can get the sum 's' without the number at index 'i'
            if dp[i-1][s]:
                dp[i][s] = True
            # check if we can find a subset to get the remaining sum
            elif num[i] <= s:
                dp[i][s] = dp[i - 1][s - num[i]]

    return dp[n - 1][sum]


# Time complexity: O(n * sum), space complexity: O(sum)
def can_partition_opt1(num, sum):
    n = len(num)

    dp = [[False for y in range(sum + 1)] for x in range(2)]

    # We always can get a 0 sum subset(empty set)
    for i in range(2):
        dp[i][0] = True

    for s in range(sum + 1):
        dp[0][s] = True if num[0] == s else False

    for i in range(1, n):
        for s in range(1, sum + 1):
            # if we can get the sum 's' without the number at index 'i'
            if dp[(i % 2) - 1][s]:
                dp[(i % 2)][s] = True
            # check if we can find a subset to get the remaining sum
            elif num[i] <= s:
                dp[(i % 2)][s] = dp[(i % 2) - 1][s - num[i]]

    return dp[(n - 1) % 2][sum]


# Time complexity: O(n * sum), space complexity: O(sum)
def can_partition_opt2(num, sum):
    n = len(num)

    dp = [False for y in range(sum + 1)]


def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))
    print("Can partition: " + str(can_partition_opt1([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition_opt1([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition_opt1([1, 3, 4, 8], 6)))


main()
