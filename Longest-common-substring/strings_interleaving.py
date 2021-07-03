# Give three strings ‘m’, ‘n’, and ‘p’, write a method to find out if ‘p’ has been formed
# by interleaving ‘m’ and ‘n’. ‘p’ would be considered interleaving ‘m’ and ‘n’ if it
# contains all the letters from ‘m’ and ‘n’ and the order of letters is preserved too.

# EX1: Input: m="abd", n="cef", p="abcdef"
#      Output: true
#      Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.

# EX2: Input: m="abd", n="cef", p="adcbef"
#      Output: false
#      Explanation: 'p' contains all the letters from 'm' and 'n' but does not preserve the order.

# EX3: Input: m="abc", n="def", p="abdccf"
#      Output: false
#      Explanation: 'p' does not contain all the letters from 'm' and 'n'.

# EX4: Input: m="abcdef", n="mnop", p="mnaobcdepf"
#      Output: true
#      Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.

def find_SI_mem(m, n, p):
    return find_SI_recursive({}, m, n, p, 0, 0, 0)


def find_SI_recursive(dp, m, n, p, mi, ni, pi):
    mLen = len(m)
    nLen = len(n)
    pLen = len(p)

    # if we have reached the end of the all the strings
    if mi == mLen and ni == nLen and pi == pLen:
        return True

    # if we have reached the end of 'p' but 'm' or 'n' still has some characters left
    if pi == pLen:
        return False

    subKey = str(mi) + "-" + str(ni) + "-" + str(pi)

    if subKey not in dp:
        b1 = False
        b2 = False

        if mi < mLen and m[mi] == p[pi]:
            b1 = find_SI_recursive(dp, m, n, p, mi + 1, ni, pi + 1)

        if ni < nLen and n[ni] == p[pi]:
            b2 = find_SI_recursive(dp, m, n, p, mi, ni + 1, pi + 1)

        dp[subKey] = b1 or b2

    return dp[subKey]


def find_SI_tab(m, n, p):
    mLen = len(m)
    nLen = len(n)
    pLen = len(p)

    # dp[mi][ni] will be storing the result of string interleaving up to p[0 ... mi + ni - 1]
    dp = [[False for _ in range(nLen + 1)] for _ in range(mLen + 1)]

    # make sure if lengths of the strings add up
    if mLen + nLen != pLen:
        return False

    for mi in range(mLen + 1):
        for ni in range(nLen + 1):
            # if 'm' and 'n' are empty, then 'p' must have been empty too.
            if mi == 0 and ni == 0:
                dp[mi][ni] = True

            # if 'm' is empty, we need to check the interleaving with 'n' only
            elif mi == 0 and n[ni - 1] == p[mi + ni - 1]:
                dp[mi][ni] = dp[mi][ni - 1]

            # if 'n' is empty, we need to check the interleaving with 'm' only
            elif ni == 0 and m[mi - 1] == p[mi + ni - 1]:
                dp[mi][ni] = dp[mi - 1][ni]

            else:
                # if the letter of 'm' and 'p' match, we take whatever is matched till mi - 1
                if mi > 0 and m[mi - 1] == p[mi + ni - 1]:
                    dp[mi][ni] = dp[mi - 1][ni]

                # if the letter of 'n' and 'p' match, we take whatever is matched till ni - 1 too
                # note the '|=', this is required when we have common letters
                if ni > 0 and n[ni - 1] == p[mi + ni - 1]:
                    dp[mi][ni] |= dp[mi][ni - 1]

    return dp[mLen][nLen]


def main():
    print(find_SI_mem("abd", "cef", "abcdef"))
    print(find_SI_mem("abd", "cef", "adcbef"))
    print(find_SI_mem("abc", "def", "abdccf"))
    print(find_SI_mem("abcdef", "mnop", "mnaobcdepf"))
    print(find_SI_tab("abd", "cef", "abcdef"))
    print(find_SI_tab("abd", "cef", "adcbef"))
    print(find_SI_tab("abc", "def", "abdccf"))
    print(find_SI_tab("abcdef", "mnop", "mnaobcdepf"))


main()
