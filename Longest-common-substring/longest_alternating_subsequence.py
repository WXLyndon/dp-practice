# Given a number sequence, find the length of its Longest Alternating Subsequence (LAS).
# A subsequence is considered alternating if its elements are in alternating order.

# A three element sequence (a1, a2, a3) will be an alternating sequence if its elements
# hold one of the following conditions: {a1 > a2 < a3 } or { a1 < a2 > a3}.

# EX1: Input: {1,2,3,4}
#      Output: 2
#      Explanation: There are many LAS: {1,2}, {3,4}, {1,3}, {1,4}

# EX2: Input: {3,2,1,4}
#      Output: 3
#      Explanation: The LAS are {3,2,4} and {2,1,4}.

# EX3: Input: {1,3,2,4}
#      Output: 4
#      Explanation: The LAS is {1,3,2,4}.

def find_LAS_length_mem(nums):
    n = len(nums)
    dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
    return max(find_LAS_length_recursive(dp, nums, -1, 0, True), find_LAS_length_recursive(dp, nums, -1, 0, False))


def find_LAS_length_recursive(dp, nums, previousIndex, currentIndex, isAsc):
    if currentIndex == len(nums):
        return 0

    if dp[previousIndex + 1][currentIndex][1 if isAsc else 0] == -1:

        c1 = 0
        # if ascending, the next element should be bigger
        if isAsc:
            if previousIndex == -1 or nums[previousIndex] < nums[currentIndex]:
                c1 = 1 + \
                    find_LAS_length_recursive(
                        dp, nums, currentIndex, currentIndex + 1, not isAsc)
        else:  # if descending, the next element should be smaller
            if previousIndex == -1 or nums[previousIndex] > nums[currentIndex]:
                c1 = 1 + \
                    find_LAS_length_recursive(
                        dp, nums, currentIndex, currentIndex + 1, not isAsc)

        # skip the current element
        c2 = find_LAS_length_recursive(
            dp, nums, previousIndex, currentIndex + 1, isAsc)
        dp[previousIndex + 1][currentIndex][1 if isAsc else 0] = max(c1, c2)

    return dp[previousIndex + 1][currentIndex][1 if isAsc else 0]


def find_LAS_length_tab(nums):
    n = len(nums)
    if n == 0:
        return 0
    # dp[i][0] = stores the LAS ending at 'i' such that the last two elements are in ascending order
    # dp[i][1] = stores the LAS ending at 'i' such that the last two elements are in descending order
    dp = [[0 for _ in range(2)] for _ in range(n)]
    maxLength = 1
    for i in range(n):
        # every single element can be considered as LAS of length 1
        dp[i][0] = dp[i][1] = 1
        for j in range(i):
            if nums[i] > nums[j]:
                # if nums[i] is BIGGER than nums[j] then we will consider the LAS ending at 'j' where the
                # last two elements were in DESCENDING order
                dp[i][0] = max(dp[i][0], 1 + dp[j][1])
                maxLength = max(maxLength, dp[i][0])
            elif nums[i] < nums[j]:  # if the numbers are equal don't do anything
                # if nums[i] is SMALLER than nums[j] then we will consider the LAS ending at
                # 'j' where the last two elements were in ASCENDING order
                dp[i][1] = max(dp[i][1], 1 + dp[j][0])
                maxLength = max(maxLength, dp[i][1])
    return maxLength


def main():
    print(find_LAS_length_mem([1, 2, 3, 4]))
    print(find_LAS_length_mem([3, 2, 1, 4]))
    print(find_LAS_length_mem([1, 3, 2, 4]))
    print(find_LAS_length_tab([1, 2, 3, 4]))
    print(find_LAS_length_tab([3, 2, 1, 4]))
    print(find_LAS_length_tab([1, 3, 2, 4]))


main()
