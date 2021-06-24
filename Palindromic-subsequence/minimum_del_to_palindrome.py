# Given a string, find the minimum number of characters that we can remove to make it a palindrome.

# EX1: Input: "abdbca"
#      Output: 1
#      Explanation: By removing "c", we get a palindrome "abdba".

# EX2: Input: = "cddpd"
#      Output: 2
#      Explanation: Deleting "cp", we get a palindrome "ddd".

# EX3: Input: = "pqr"
#      Output: 2
#      Explanation: We have to remove any two characters to get a palindrome, e.g. if we
#      remove "pq", we get palindrome "r".

def find_minimum_deletions(st):
    # subtracting the length of Longest Palindromic Subsequence from the length of
    # the input string to get minimum number of deletions
    return len(st) - find_LPS_length(st)


def find_LPS_length(st):
    n = len(st)
    # dp[i][j] stores the length of LPS from index 'i' to index 'j'
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # every sequence with one element is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            # case 1: elements at the beginning and the end are the same
            if st[startIndex] == st[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:  # case 2: skip one element either from the beginning or the end
                dp[startIndex][endIndex] = max(
                    dp[startIndex + 1][endIndex], dp[startIndex][endIndex - 1])

    return dp[0][n - 1]


def main():
    print(find_minimum_deletions("abdbca"))
    print(find_minimum_deletions("cddpd"))
    print(find_minimum_deletions("pqr"))


main()
