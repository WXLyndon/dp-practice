# Given a number sequence, find the length of its Longest Increasing Subsequence (LIS). In an increasing subsequence,
# all the elements are in increasing order (from lowest to highest).

# EX1: Input: {4,2,3,6,10,1,12}
#      Output: 5
#      Explanation: The LIS is {2,3,6,10,12}.

# EX2: Input: {-4,10,3,7,15}
#      Output: 4
#      Explanation: The LIS is {-4,3,7,15}.

def find_LIS_length_mem(nums):
    n = len(nums)
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

    return find_LCS_length_recursive(nums, dp, 0, -1)


def find_LCS_length_recursive(nums, dp, currentIndex, previousIndex):
    if currentIndex == len(nums):
        return 0

    if dp[currentIndex][previousIndex + 1] == -1:
        # include nums[currentIndex] if it is larger than the last included number
        l1 = 0
        if previousIndex == -1 or nums[currentIndex] > nums[previousIndex]:
            l1 = 1 + \
                find_LCS_length_recursive(
                    nums, dp, currentIndex + 1, currentIndex)

        l2 = find_LCS_length_recursive(
            nums, dp, currentIndex + 1, previousIndex)

        dp[currentIndex][previousIndex + 1] = max(l1, l2)

    return dp[currentIndex][previousIndex + 1]


def find_LIS_length_tab(nums):
    n = len(nums)
    dp = [0 for _ in range(n)]
    dp[0] = 1

    maxLength = 1
    for i in range(1, n):
        dp[i] = 1
        for j in range(i):
            if nums[i] > nums[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
                maxLength = max(maxLength, dp[i])

    return maxLength


def main():
    print(find_LIS_length_mem([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS_length_mem([-4, 10, 3, 7, 15]))
    print(find_LIS_length_tab([4, 2, 3, 6, 10, 1, 12]))
    print(find_LIS_length_tab([-4, 10, 3, 7, 15]))


main()
