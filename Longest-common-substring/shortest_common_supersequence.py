# Given two sequences ‘s1’ and ‘s2’, write a method to find the length of the shortest
# sequence which has ‘s1’ and ‘s2’ as subsequences.

# EX1: Input: s1: "abcf" s2:"bdcf"
#      Output: 5
#      Explanation: The shortest common super-sequence (SCS) is "abdcf".

# EX2: Input: s1: "dynamic" s2:"programming"
#      Output: 15
#      Explanation: The SCS is "dynprogrammicng".

def find_SCS_length_mem(s1, s2):
    dp = [[-1 for _ in range(len(s2))] for _ in range(len(s1))]

    return find_SCS_length_recursive(dp, s1, s2, 0, 0)


def find_SCS_length_recursive(dp, s1, s2, i1, i2):
    n1 = len(s1)
    n2 = len(s2)

    # if we have reached the end of a string, return the remaining length of the
    # other string, as in this case we have to take all of the remaining other string
    if i1 == n1:
        return n2 - i2
    if i2 == n2:
        return n1 - i1

    if dp[i1][i2] == -1:
        if s1[i1] == s2[i2]:
            dp[i1][i2] = 1 + \
                find_SCS_length_recursive(dp, s1, s2, i1 + 1, i2 + 1)
        else:
            l1 = 1 + find_SCS_length_recursive(dp, s1, s2, i1 + 1, i2)
            l2 = 1 + find_SCS_length_recursive(dp, s1, s2, i1, i2 + 1)
            dp[i1][i2] = min(l1, l2)

    return dp[i1][i2]


def find_SCS_length_tab(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # if one of the strings is of zero length, SCS would be
    # equal to the length of the other string

    for i in range(n1 + 1):
        dp[i][0] = i
    for j in range(n2 + 1):
        dp[0][j] = j

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    return dp[n1][n2]


def main():
    print(find_SCS_length_mem("abcf", "bdcf"))
    print(find_SCS_length_mem("dynamic", "programming"))
    print(find_SCS_length_tab("abcf", "bdcf"))
    print(find_SCS_length_tab("dynamic", "programming"))


main()
