"""
Problem Statement
Given a number 'n', implement a method to count how many possible ways there are to express 'n' as the sum of 1, 3, or 4.

Example 1:

n : 4
Number of ways = 4
Explanation: Following are the four ways we can express 'n' : {1,1,1,1}, {1,3}, {3,1}, {4}
Example 2:

n : 5
Number of ways = 6
Explanation: Following are the six ways we can express 'n' : {1,1,1,1,1}, {1,1,3}, {1,3,1}, {3,1,1},
{1,4}, {4,1}
Let's first start with a recursive brute-force solution.
"""


def count_ways_iterative(n):
    dp = [0] * max(n + 1, 4)
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 3] + dp[i - 4]

    return dp[n]


def count_ways_recursive(n):
    dp = [-1] * (n + 1)
    return recurse(n, dp)


def recurse(n, dp):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if dp[n] > -1:
        return dp[n]
    one = recurse(n - 1, dp)
    two = recurse(n - 3, dp)
    three = recurse(n - 4, dp)
    dp[n] = one + two + three
    return dp[n]
