# Given a number array to represent possible ribbon lengths and a total ribbon length ‘n,’ we need to find the
# maximum number of pieces that the ribbon can be cut into.

# EX 1: n: 5
#       Ribbon Lengths: {2,3,5}
#       Output: 2
#       Explanation: Ribbon pieces will be {2,3}.

# EX 2: n: 7
#       Ribbon Lengths: {2,3}
#       Output: 3
#       Explanation: Ribbon pieces will be {2,2,3}.

# EX 3: n: 13
#       Ribbon Lengths: {3,5,7}
#       Output: 3
#       Explanation: Ribbon pieces will be {3,3,7}.

def count_ribbon_pieces_mem(ribbonLengths, total):
    maxPieces = count_ribbon_pieces_recursive(ribbonLengths, total, 0)
    return -1 if maxPieces == float("-inf") else maxPieces


def count_ribbon_pieces_recursive(ribbonLengths, total, currentIndex):
    if total == 0:
        return 0

    n = len(ribbonLengths)
    if n == 0 or currentIndex >= n:
        return float("-inf")

    c1 = float("-inf")
    if ribbonLengths[currentIndex] <= total:
        result = count_ribbon_pieces_recursive(ribbonLengths, total - ribbonLengths[currentIndex], currentIndex)
        if result != float("-inf"):
            c1 = result + 1

    c2 = count_ribbon_pieces_recursive(ribbonLengths, total, currentIndex + 1)

    return max(c1, c2)


def count_ribbon_pieces_tab(ribbonLengths, total):
    n = len(ribbonLengths)

    dp = [[float("-inf") for _ in range(total + 1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for j in range(1, total + 1):
            if i > 0:
                dp[i][j] = dp[i - 1][j]

            if ribbonLengths[i] <= j and dp[i][j - ribbonLengths[i]] != float("-inf"):
                dp[i][j] = max(dp[i][j], dp[i][j - ribbonLengths[i]] + 1)

    return -1 if dp[n - 1][total] == float("-inf") else dp[n - 1][total]


def main():
    print(count_ribbon_pieces_mem([2, 3, 5], 5))
    print(count_ribbon_pieces_mem([2, 3], 7))
    print(count_ribbon_pieces_mem([3, 5, 7], 13))
    print(count_ribbon_pieces_mem([3, 5], 7))
    print(count_ribbon_pieces_tab([2, 3, 5], 5))
    print(count_ribbon_pieces_tab([2, 3], 7))
    print(count_ribbon_pieces_tab([3, 5, 7], 13))
    print(count_ribbon_pieces_tab([3, 5], 7))


main()
