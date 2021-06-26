# Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters.
# Write a function to calculate the count of the minimum number of deletion and insertion operations.


# EX1: Input: s1 = "abc"
#             s2 = "fbc"
#      Output: 1 deletion and 1 insertion.
#      Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.

# EX2: Input: s1 = "abdca"
#             s2 = "cbda"
#      Output: 2 deletions and 1 insertion.
#      Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.

# EX3: Input: s1 = "passport"
#             s2 = "ppsspt"
#      Output: 3 deletions and 1 insertion
#      Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.

def find_MDI(s1, s2):
    c1 = find_LCS_length(s1, s2)
    print("Minimum deletions needed: " + str(len(s1) - c1))
    print("Minimum insertions needed: " + str(len(s2) - c1))


def find_LCS_length(s1, s2):
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


def main():
    find_MDI("abc", "fbc")
    find_MDI("abdca", "cbda")
    find_MDI("passport", "ppsspt")


main()
