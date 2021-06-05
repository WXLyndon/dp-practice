# Given an array of positive numbers, where each element represents the max number of jumps that
# can be made forward from that element, write a program to find the minimum number of jumps needed
# to reach the end of the array (starting from the first element). If an element is 0, then we cannot
# move through that element.

# EX1: Input = {2,1,1,1,4}
#      Output = 3
#      Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4

# EX2: Input = {1,1,3,6,9,3,0,1,3}
#      Output = 4
# Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8


def count_min_jumps_mem(jumps):
    dp = [0 for _ in range(len(jumps))]
    return count_min_jumps_recursive(dp, jumps, 0)


def count_min_jumps_recursive(dp, jumps, currentIndex):
    n = len(jumps)

    # reach the last index, no need to jump
    if currentIndex == n - 1:
        return 0

    # cannot jump at this index
    if jumps[currentIndex] == 0:
        return float("inf")

    # this sub-problem is already solved
    if dp[currentIndex] != 0:
        return dp[currentIndex]

    total = float("inf")
    start = currentIndex + 1
    end = currentIndex + jumps[currentIndex]
    while start < n and start <= end:
        # jump one step and recurse the remaining arrays
        minJumps = count_min_jumps_recursive(dp, jumps, start)
        start += 1
        if minJumps != float("inf"):
            total = min(total, minJumps + 1)

    dp[currentIndex] = total

    return dp[currentIndex]


def count_min_jumps_tab(jumps):
    n = len(jumps)
    dp = [float("inf") for _ in range(n)]
    dp[0] = 0

    for start in range(n - 1):
        end = start + 1
        while end <= start + jumps[start] and end < n:
            dp[end] = min(dp[end], dp[start] + 1)
            end += 1
    return dp[n - 1]


def main():
    print(count_min_jumps_mem([2, 1, 1, 1, 4]))
    print(count_min_jumps_mem([1, 1, 3, 6, 9, 3, 0, 1, 3]))
    print(count_min_jumps_tab([2, 1, 1, 1, 4]))
    print(count_min_jumps_tab([1, 1, 3, 6, 9, 3, 0, 1, 3]))


main()
