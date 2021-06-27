# Given a number sequence, find the increasing subsequence with the highest sum. Write a method that returns the highest sum.

# EX1: Input: {4,2,3,6,10,1,12}
#      Output: 32
#      Explanation: The increaseing sequence is {4,6,10,12}. Please note the difference,
#                   as the LIS is {1,2,6,10,12} which has a sum of '31'.

# EX2: Input: {-4,10,3,7,15}
#      Output: 25
#      Explanation: The increaseing sequences are {10, 15} and {3,7,15}.


def find_MSIS_mem(nums):
    dp = {}
    return find_MSIS_recursive(nums, dp, 0, -1, 0)


def find_MSIS_recursive(nums, dp, currentIndex, previousIndex, sum):
    if currentIndex == len(nums):
        return sum

    subProblemKey = str(currentIndex) + "-" + \
        str(previousIndex) + "-" + str(sum)

    if subProblemKey not in dp:

        # include nums[currentIndex] if it is larger than the last included number
        s1 = sum
        if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
            s1 = find_MSIS_recursive(
                nums, dp, currentIndex + 1, currentIndex, sum + nums[currentIndex])

        # excluding the number at currentIndex
        s2 = find_MSIS_recursive(
            nums, dp, currentIndex + 1, previousIndex, sum)

        dp[subProblemKey] = max(s1, s2)

    return dp[subProblemKey]


def find_MSIS_tab(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = nums[0]

    maxSum = dp[0]

    for i in range(1, n):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]

        maxSum = max(maxSum, dp[i])

    return maxSum


def main():
    print(find_MSIS_mem([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS_mem([-4, 10, 3, 7, 15]))
    print(find_MSIS_tab([4, 1, 2, 6, 10, 1, 12]))
    print(find_MSIS_tab([-4, 10, 3, 7, 15]))


main()
