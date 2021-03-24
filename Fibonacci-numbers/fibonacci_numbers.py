def calculateFibonacciMem(n):
    dp = [-1 for x in range(n + 1)]
    return calculateFibonacciRecur(dp, n)


def calculateFibonacciRecur(dp, n):
    if n < 2:
        return n

    if dp[n] >= 0:
        return dp[n]

    dp[n] = calculateFibonacciRecur(dp, n - 1) + calculateFibonacciRecur(dp, n - 2)

    return dp[n]


def calculateFibonacciTab(n):
    if n < 2:
        return n

    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])

    return dp[n]


def main():
    print("5th Fibonacci is ---> " + str(calculateFibonacciMem(5)))
    print("6th Fibonacci is ---> " + str(calculateFibonacciMem(6)))
    print("7th Fibonacci is ---> " + str(calculateFibonacciMem(7)))
    print("5th Fibonacci is ---> " + str(calculateFibonacciTab(5)))
    print("6th Fibonacci is ---> " + str(calculateFibonacciTab(6)))
    print("7th Fibonacci is ---> " + str(calculateFibonacciTab(7)))


main()
