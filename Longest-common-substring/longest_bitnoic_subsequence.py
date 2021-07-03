# Given a number sequence, find the length of its Longest Bitonic Subsequence (LBS).
# A subsequence is considered bitonic if it is monotonically increasing and then
# monotonically decreasing.

# EX1: Input: {4,2,3,6,10,1,12}
#      Output: 5
#      Explanation: The LBS is {2,3,6,10,1}.

# EX2: Input: {4,2,5,9,7,6,10,3,1}
#      Output: 7
#      Explanation: The LBS is {4,5,9,7,6,3,1}.


def find_LBS_length_mem(nums):
    n = len(nums)

    lds = [[-1 for _ in range(n + 1)] for _ in range(n)]
    ldsReverse = [[-1 for _ in range(n + 1)] for _ in range(n)]

    maxLength = 0
    for i in range(n):
        l1 = find_LBS_length_recursive(lds, nums, i, -1)
        l2 = find_LBS_length_recursive_reverse(ldsReverse, nums, i, -1)
        maxLength = max(maxLength, l1 + l2 - 1)

    return maxLength


# find the longest decreasing subsequence from currentIndex till the end of the array
def find_LBS_length_recursive(dp, nums, currentIndex, previousIndex):
    if currentIndex == len(nums):
        return 0

    if dp[currentIndex][previousIndex + 1] == -1:
        # include nums[currentIndex] if it is smaller than the previous number
        c1 = 0

        if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
            c1 = 1 + \
                find_LBS_length_recursive(
                    dp, nums, currentIndex + 1, currentIndex)

        # excluding the number at currentIndex
        c2 = find_LBS_length_recursive(
            dp, nums, currentIndex + 1, previousIndex)

        dp[currentIndex][previousIndex + 1] = max(c1, c2)

    return dp[currentIndex][previousIndex + 1]


# find the longest decreasing subsequence from currentIndex till the beginning of the array
def find_LBS_length_recursive_reverse(dp, nums, currentIndex, previousIndex):
    if currentIndex < 0:
        return 0

    if dp[currentIndex][previousIndex + 1] == -1:

        # include nums[currentIndex] if it is smaller than the previous number
        c1 = 0
        if previousIndex == -1 or nums[currentIndex] < nums[previousIndex]:
            c1 = 1 + \
                find_LBS_length_recursive_reverse(
                    dp, nums, currentIndex - 1, currentIndex)

        # excluding the number at currentIndex
        c2 = find_LBS_length_recursive_reverse(
            dp, nums, currentIndex - 1, previousIndex)

        dp[currentIndex][previousIndex + 1] = max(c1, c2)

    return dp[currentIndex][previousIndex + 1]


def find_LBS_length_tab(nums):
    n = len(nums)
    lds = [0 for _ in range(n)]
    ldsReverse = [0 for _ in range(n)]

    # find LDS for every index up to the beginning of the array
    for i in range(n):
        lds[i] = 1  # every element is an LDS of length 1
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                lds[i] = max(lds[i], lds[j] + 1)

    # find LDS for every index up to the end of the array
    for i in range(n - 1, -1, -1):
        ldsReverse[i] = 1  # every element is an LDS of length 1
        for j in range(i + 1, n):
            if nums[j] < nums[i]:
                ldsReverse[i] = max(ldsReverse[i], ldsReverse[j] + 1)

    maxLength = 0
    for i in range(n):
        maxLength = max(maxLength, lds[i] + ldsReverse[i] - 1)

    return maxLength


def main():
    print(find_LBS_length_mem([4, 2, 3, 6, 10, 1, 12]))
    print(find_LBS_length_mem([4, 2, 5, 9, 7, 6, 10, 3, 1]))
    print(find_LBS_length_tab([4, 2, 3, 6, 10, 1, 12]))
    print(find_LBS_length_tab([4, 2, 5, 9, 7, 6, 10, 3, 1]))


main()
