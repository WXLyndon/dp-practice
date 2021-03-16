# Given a set of positive numbers, partition the set into two subsets with a minimum difference between their subset sums.

# EX 1: IInput: {1, 2, 3, 9}
#       Output: 3
#       Explanation: We can partition the given set into two subsets where minimum absolute difference 
#       between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
# EX 2: Input: {1, 2, 7, 1, 5}
#       Output: 0
#       Explanation: We can partition the given set into two subsets where minimum absolute difference 
#       between the sum of number is '0'. Following are the two subsets: {1, 2, 5} & {7, 1}.
# EX 3: Input: {1, 3, 100, 4}
#       Output: 92
#       Explanation: We can partition the given set into two subsets where minimum absolute difference 
#       between the sum of numbers is '92'. Here are the two subsets: {1, 3, 4} & {100}.

# Time complexity: O(n * sum), space complexity: O(n * sum)
def can_partition(num):
    s = sum(num)
    n = len(num)
    half = s // 2
    dp = [[False for y in range(half + 1)] for x in range(n)]

    for i in range(n):
        dp[i][0] = True
    
    for i in range(1, half + 1):
        dp[0][i] = True if num[0] == i else False
    
    for i in range(1, n):
        for j in range(1, half + 1):

            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif num[i] <= j:
                dp[i][j] = dp[i - 1][j - num[i]]
    
    sum1 = 0
    # Find the largest index in the last row which is true
    for i in range(half, -1, -1):
        if dp[n - 1][i]:
            sum1 = i
            break
    
    sum2 = s - sum1

    return abs(sum2 - sum1)

def main():
  print("Can partition: " + str(can_partition([1, 2, 3, 9])))
  print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
  print("Can partition: " + str(can_partition([1, 3, 100, 4])))


main()