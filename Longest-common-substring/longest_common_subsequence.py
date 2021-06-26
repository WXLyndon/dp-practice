# Given two strings ‘s1’ and ‘s2’, find the length of the longest subsequence which is common in both the strings.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements
# without changing the order of the remaining elements.


# EX1: Input: s1 = "abdca"
#             s2 = "cbda"
#      Output: 2
#      Explanation: The longest common substring is "bd".


# EX2: Input: s1 = "passport"
#             s2 = "ppsspt"
#      Output: 3
#      Explanation: The longest common substring is "ssp".

def find_LCS_length_mem(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]
    return find_LCS_length_recursive(dp, s1, s2, 0, 0)


def find_LCS_length_recursive(dp, s1, s2, i1, i2):
    if i1 == len(s1) or i2 == len(s2):
        return 0

    if dp[i1][i2] == -1:

        if s1[i1] == s2[i2]:
            dp[i1][i2] = 1 + \
                find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2 + 1)
        else:
            c1 = find_LCS_length_recursive(dp, s1, s2, i1 + 1, i2)
            c2 = find_LCS_length_recursive(dp, s1, s2, i1, i2 + 1)
            dp[i1][i2] = max(c1, c2)

    return dp[i1][i2]


def find_LCS_length_tab(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
    maxLength = 0

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

            maxLength = max(maxLength, dp[i][j])

    return maxLength


def find_LCS_length_opt(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(2)]
    maxLength = 0

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i % 2][j] = 1 + dp[(i - 1) % 2][j - 1]
            else:
                dp[i % 2][j] = max(dp[(i - 1) % 2][j], dp[i % 2][j - 1])

            maxLength = max(maxLength, dp[i % 2][j])

    return maxLength


def main():
    print(find_LCS_length_mem("abdca", "cbda"))
    print(find_LCS_length_mem("passport", "ppsspt"))
    print(find_LCS_length_tab("abdca", "cbda"))
    print(find_LCS_length_tab("passport", "ppsspt"))
    print(find_LCS_length_opt("abdca", "cbda"))
    print(find_LCS_length_opt("passport", "ppsspt"))


main()
