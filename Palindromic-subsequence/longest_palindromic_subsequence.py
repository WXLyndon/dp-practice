# Given a sequence, find the length of its Longest Palindromic Subsequence (LPS).
# In a palindromic subsequence, elements read the same backward and forward.

# A subsequence is a sequence that can be derived from another sequence by
# deleting some or no elements without changing the order of the remaining elements.

# EX1: Input: "abdbca"
#      Output: 5
#      Explanation: LPS is "abdba".

# EX2: Input: = "cddpd"
#      Output: 3
#      Explanation: LPS is "ddd".

# EX3: Input: = "pqr"
#      Output: 1
#      Explanation: LPS could be "p", "q" or "r".


def find_LPS_length_mem(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_LPS_length_recursive(dp, st, 0, n - 1)


def find_LPS_length_recursive(dp, st, startIndex, endIndex):
    if startIndex > endIndex:
        return 0

    if startIndex == endIndex:
        return 1

    if (dp[startIndex][endIndex] == -1):
        # case 1: chars at startIndex and endIndex are the same
        if st[startIndex] == st[endIndex]:
            dp[startIndex][endIndex] = 2 + \
                find_LPS_length_recursive(dp, st, startIndex + 1, endIndex - 1)
        else:
            # case 2: skip one char either from the startIndex or the endIndex
            l1 = find_LPS_length_recursive(dp, st, startIndex + 1, endIndex)
            l2 = find_LPS_length_recursive(dp, st, startIndex, endIndex - 1)
            dp[startIndex][endIndex] = max(l1, l2)

    return dp[startIndex][endIndex]


def find_LPS_length_tab(st):
    n = len(st)

    dp = [[0 for _ in range(n)] for _ in range(n)]

    # every sequence with one element is a palindrome of length 1
    for i in range(n):
        dp[i][i] = 1

    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            # case 1: chars at startIndex and endIndex are the same
            if st[startIndex] == st[endIndex]:
                dp[startIndex][endIndex] = 2 + dp[startIndex + 1][endIndex - 1]
            else:
                # case 2: skip one char either from the startIndex or the endIndex
                l1 = dp[startIndex + 1][endIndex]
                l2 = dp[startIndex][endIndex - 1]
                dp[startIndex][endIndex] = max(l1, l2)

    return dp[0][n - 1]


def main():
    print(find_LPS_length_mem("abdbca"))
    print(find_LPS_length_mem("cddpd"))
    print(find_LPS_length_mem("pqr"))
    print(find_LPS_length_mem("absdfcdcghkjba"))  # abcdcba
    print(find_LPS_length_tab("abdbca"))
    print(find_LPS_length_tab("cddpd"))
    print(find_LPS_length_tab("pqr"))
    print(find_LPS_length_tab("absdfcdcghkjba"))


main()
