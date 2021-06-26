# Given a string, we want to cut it into pieces such that each piece is a palindrome.
# Write a function to return the minimum number of cuts needed.

# EX1: Input: "abdbca"
#      Output: 3
#      Explanation: Palindrome pieces are "a", "bdb", "c", "a".

# EX2: Input: = "cddpd"
#      Output: 2
#      Explanation: Palindrome pieces are "c", "d", "dpd".

# EX3: Input: = "pqr"
#      Output: 2
#      Explanation: Palindrome pieces are "p", "q", "r".

# EX4: Input: = "pp"
#      Output: 0
#      Explanation: We do not need to cut, as "pp" is a palindrome.


def is_palindrome(st, palindromeDp, startIndex, endIndex):
    if palindromeDp[startIndex][endIndex] == -1:
        palindromeDp[startIndex][endIndex] = 1
        i = startIndex
        j = endIndex
        while i < j:
            if st[i] != st[j]:
                palindromeDp[startIndex][endIndex] = 0
                break
            i += 1
            j -= 1
            # use memoization to find if the remaining string is a palindrome
            if i < j and palindromeDp[i][j] != -1:
                palindromeDp[startIndex][endIndex] = palindromeDp[i][j]
                break

    return palindromeDp[startIndex][endIndex] == 1


def find_MPP_cuts_mem(st):
    n = len(st)
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    palindromeDp = [[-1 for _ in range(n)] for _ in range(n)]
    return find_MPP_cuts_recursive(st, dp, palindromeDp, 0, n - 1)


def find_MPP_cuts_recursive(st, dp, palindromeDp, startIndex, endIndex):
    if startIndex >= endIndex or is_palindrome(st, palindromeDp, startIndex, endIndex):
        return 0

    if dp[startIndex][endIndex] == -1:
        # at max, we need to cut the string into its 'length-1' pieces
        minCuts = endIndex - startIndex

        for i in range(startIndex, endIndex + 1):
            if is_palindrome(st, palindromeDp, startIndex, i):
              # we can cut here as we have a palindrome from 'startIndex' to 'i'
                minCuts = min(
                    minCuts, 1 + find_MPP_cuts_recursive(st, dp, palindromeDp, i + 1, endIndex))

        dp[startIndex][endIndex] = minCuts

    return dp[startIndex][endIndex]


def find_MPP_cuts_tab(st):
    n = len(st)
    # isPalindrome[i][j] will be 'true' if the string from index 'i' to index 'j' is a palindrome
    palindromeDp = [[False for _ in range(n)] for _ in range(n)]

    # every string with only one char is a palindrome
    for i in range(n):
        palindromeDp[i][i] = True

    # populate isPalindrome table
    for startIndex in range(n - 1, -1, -1):
        for endIndex in range(startIndex + 1, n):
            if st[startIndex] == st[endIndex]:
                # if it's a two character string or if the remaining string is a palindrome too
                if endIndex - startIndex == 1 or palindromeDp[startIndex + 1][endIndex - 1]:
                    palindromeDp[startIndex][endIndex] = True

    # now lets populate the second table, every index in 'cuts' stores the minimum cuts needed
    # for the substring from that index till the end
    dp = [0 for _ in range(n)]
    for startIndex in range(n - 1, -1, -1):
        minCuts = n  # maximum cuts
        for endIndex in range(n - 1, startIndex - 1, -1):
            if palindromeDp[startIndex][endIndex]:
                # we can cut here as we got a palindrome
                # also we don't need any cut if the whole substring is a palindrome
                minCuts = 0 if endIndex == n - \
                    1 else min(minCuts, 1 + dp[endIndex + 1])
        dp[startIndex] = minCuts

    return dp[0]


def main():
    print(find_MPP_cuts_mem("abdbca"))
    print(find_MPP_cuts_mem("cdpdd"))
    print(find_MPP_cuts_mem("pqr"))
    print(find_MPP_cuts_mem("pp"))
    print(find_MPP_cuts_mem("madam"))
    print(find_MPP_cuts_tab("abdbca"))
    print(find_MPP_cuts_tab("cdpdd"))
    print(find_MPP_cuts_tab("pqr"))
    print(find_MPP_cuts_tab("pp"))
    print(find_MPP_cuts_tab("madam"))


main()
