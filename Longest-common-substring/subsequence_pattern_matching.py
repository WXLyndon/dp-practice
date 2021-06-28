# Given a string and a pattern, write a method to count the number of times the pattern
# appears in the string as a subsequence.

# EX1: Input: string: “baxmx”, pattern: “ax”
#      Output: 2
#      Explanation: {baxmx, baxmx}.

# EX2: Input: string: “tomorrow”, pattern: “tor”
#      Output: 4
#      Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.

def find_SPM_count_mem(str, pat):
    dp = [[-1 for _ in range(len(pat))] for _ in range(len(str))]

    return find_SPM_count_recursive(dp, str, pat, 0, 0)


def find_SPM_count_recursive(dp, str, pat, strIndex, patIndex):

    # if we have reached the end of the pattern
    if patIndex == len(pat):
        return 1

     # if we have reached the end of the string but pattern has still some characters left
    if strIndex == len(str):
        return 0

    if dp[strIndex][patIndex] == -1:

        c1 = 0
        if str[strIndex] == pat[patIndex]:
            c1 = find_SPM_count_recursive(
                dp, str, pat, strIndex + 1, patIndex + 1)

        c2 = find_SPM_count_recursive(dp, str, pat, strIndex + 1, patIndex)
        dp[strIndex][patIndex] = c1 + c2

    return dp[strIndex][patIndex]


def find_SPM_count_tab(str, pat):
    strLen = len(str)
    patLen = len(pat)

    if patLen == 0:
        return 1

    if strLen == 0 or patLen > strLen:
        return 0

    # dp[strIndex][patIndex] will be storing the count of SPM up to str[0..strIndex-1][0..patIndex-1]
    dp = [[0 for _ in range(patLen + 1)] for _ in range(strLen + 1)]

    # for the empty pattern, we have one matching
    for i in range(strLen + 1):
        dp[i][0] = 1

    for strIndex in range(1, strLen + 1):
        for patIndex in range(1, patLen + 1):

            if str[strIndex - 1] == pat[patIndex - 1]:
                dp[strIndex][patIndex] = dp[strIndex - 1][patIndex - 1]
            dp[strIndex][patIndex] += dp[strIndex - 1][patIndex]

    return dp[strLen][patLen]


def main():
    print(find_SPM_count_mem("baxmx", "ax"))
    print(find_SPM_count_mem("tomorrow", "tor"))
    print(find_SPM_count_tab("baxmx", "ax"))
    print(find_SPM_count_tab("tomorrow", "tor"))


main()
