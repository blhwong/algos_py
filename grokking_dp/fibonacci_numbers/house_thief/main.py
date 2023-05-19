"""
There are n houses built in a line. A thief wants to steal the maximum possible money from these houses. The only restriction the thief has is that he can't steal from two consecutive houses, as that would alert the security system. How should the thief maximize his stealing?

Problem Statement
Given a number array representing the wealth of n houses, determine the maximum amount of money the thief can steal without alerting the security system.

Example 1:

Input: {2, 5, 1, 3, 6, 2, 4}
Output: 15
Explanation: The thief should steal from houses 5 + 6 + 4
Example 2:

Input: {2, 10, 14, 8, 1}
Output: 18
Explanation: The thief should steal from houses 10 + 8
"""


def find_max_steal_iterative(wealth):
    if len(wealth) <= 2:
        return max(wealth)

    dp = [-float('infinity')] * (len(wealth))

    dp[0] = wealth[0]
    dp[1] = max(wealth[0], wealth[1])

    for i in range(2, len(wealth)):
        dp[i] = max(dp[i - 1], wealth[i] + dp[i - 2])

    return dp[-1]


def find_max_steal_recursive(wealth):
    dp = [-1] * len(wealth)
    return recurse(wealth, 0, dp)


def recurse(wealth, i, dp):
    if i >= len(wealth):
        return 0

    if dp[i] > -1:
        return dp[i]

    steal = wealth[i] + recurse(wealth, i + 2, dp)
    skip = recurse(wealth, i + 1, dp)

    dp[i] = max(steal, skip)

    return dp[i]
