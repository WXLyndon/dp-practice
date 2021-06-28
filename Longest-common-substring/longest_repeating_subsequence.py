# Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence
# will be the one that appears at least twice in the original sequence and is not overlapping
# (i.e. none of the corresponding characters in the repeating subsequences have the same index).

# EX1: Input: “t o m o r r o w”
#      Output: 2
#      Explanation: The longest repeating subsequence is “or” {tomorrow}.

# EX2: Input: “a a b d b c e c”
#      Output: 3
#      Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.

# EX3: Input: “f m f f”
#      Output: 2
#      Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}.
#                   Please note the second last character is shared in LRS.


def find_LRS_length_mem(str):
    n = len(str)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LRS_length_recursive(str, dp, 0, 0)


def find_LRS_length_recursive(str, dp, i1, i2):
    n = len(str)
    if i1 == n or i2 == n:
        return 0

    if dp[i1][i2] == -1:
        if i1 != i2 and str[i1] == str[i2]:
            dp[i1][i2] = 1 + find_LRS_length_recursive(str, dp, i1 + 1, i2 + 1)
        else:
            l1 = find_LRS_length_recursive(str, dp, i1 + 1, i2)
            l2 = find_LRS_length_recursive(str, dp, i1, i2 + 1)
            dp[i1][i2] = max(l1, l2)

    return dp[i1][i2]


def find_LRS_length_tab(str):
    n = len(str)
    dp = [[0 for i in range(n + 1)] for _ in range(n + 1)]
    maxLength = 0

    # dp[i1][i2] will be storing the LRS up to str[0..i1-1][0..i2-1]
    # this also means that subsequences of length zero(first row and column of
    # dp[][]), will always have LRS of size zero.

    for i in range(1, n + 1):
        for j in range(1, n + 1):

            if i != j and str[i - 1] == str[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            maxLength = max(maxLength, dp[i][j])

    return maxLength


def main():
    print(find_LRS_length_mem("tomorrow"))
    print(find_LRS_length_mem("aabdbcec"))
    print(find_LRS_length_mem("fmff"))
    print(find_LRS_length_tab("tomorrow"))
    print(find_LRS_length_tab("aabdbcec"))
    print(find_LRS_length_tab("fmff"))


main()
