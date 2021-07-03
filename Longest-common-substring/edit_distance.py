# Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting,
# or replacing characters. Write a function to calculate the count of the minimum number of edit operations.

# EX1: Input: s1 = "bat"
#             s2 = "but"
#      Output: 1
#      Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.

# EX2: Input: s1 = "abdca"
#             s2 = "cbda"
#      Output: 2
#      Explanation: We can replace first 'a' with 'c' and delete second 'c'.

# EX3: Input: s1 = "passpot"
#             s2 = "ppsspqrt"
#      Output: 3
#      Explanation: Replace 'a' with 'p', 'o' with 'q', and insert 'r'.

def find_min_operations_mem(s1, s2):
    dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
    return find_min_operations_recursive(dp, s1, s2, 0, 0)


def find_min_operations_recursive(dp, s1, s2, i1, i2):
    n1 = len(s1)
    n2 = len(s2)

    if dp[i1][i2] == -1:
        # if we have reached the end of s1, then we have to insert all the remaining  characters of s2
        if i1 == n1:
            dp[i1][i2] = n2 - i2

        # if we have reached the end of s2, then we have to delete all the remaining characters of s1
        elif i2 == n2:
            dp[i1][i2] = n1 - i1

        # If the strings have a matching character, we can recursively match for the remaining lengths
        elif s1[i1] == s2[i2]:
            dp[i1][i2] = find_min_operations_recursive(
                dp, s1, s2, i1 + 1, i2 + 1)
        else:
            c1 = find_min_operations_recursive(
                dp, s1, s2, i1 + 1, i2)  # delete
            c2 = find_min_operations_recursive(
                dp, s1, s2, i1, i2 + 1)  # insert
            c3 = find_min_operations_recursive(
                dp, s1, s2, i1 + 1, i2 + 1)  # replace

            dp[i1][i2] = 1 + min(c1, min(c2, c3))

    return dp[i1][i2]


def find_min_operations_tab(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2 + 1)] for _ in range(n1 + 1)]

    # if s2 is empty, we can remove all the characters of s1 to make it empty too
    for i1 in range(n1 + 1):
        dp[i1][0] = i1

    # if s1 is empty, we have to insert all the characters of s2
    for i2 in range(n2+1):
        dp[0][i2] = i2

    for i1 in range(1, n1 + 1):
        for i2 in range(1, n2 + 1):
            # If the strings have a matching character, we can recursively match for the remaining lengths
            if s1[i1 - 1] == s2[i2 - 1]:
                dp[i1][i2] = dp[i1 - 1][i2 - 1]
            else:
                dp[i1][i2] = 1 + min(dp[i1 - 1][i2],  # delete
                                     min(dp[i1][i2 - 1],  # insert
                                         dp[i1 - 1][i2 - 1]))  # replace
    return dp[n1][n2]


def main():
    print(find_min_operations_mem("bat", "but"))
    print(find_min_operations_mem("abdca", "cbda"))
    print(find_min_operations_mem("passpot", "ppsspqrt"))
    print(find_min_operations_tab("bat", "but"))
    print(find_min_operations_tab("abdca", "cbda"))
    print(find_min_operations_tab("passpot", "ppsspqrt"))


main()
