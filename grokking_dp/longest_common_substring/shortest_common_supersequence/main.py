"""
Problem Statement
Given two sequences 's1' and 's2', write a method to find the length of the shortest sequence which has 's1' and 's2' as subsequences.

Example 2:

Input: s1: "abcf" s2:"bdcf"
Output: 5
Explanation: The shortest common super-sequence (SCS) is "abdcf".
Example 2:

Input: s1: "dynamic" s2:"programming"
Output: 15
Explanation: The SCS is "dynprogrammicng".
"""


def find_scs_length_iterative(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        dp[i][0] = i

    for j in range(len(s2) + 1):
        dp[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


def find_scs_length_recursive(s1, s2):
    dp = [[0] * len(s2) for _ in range(len(s1))]
    return recurse(s1, s2, 0, 0, dp)


def recurse(s1, s2, i, j, dp):
    if i >= len(s1):
        return len(s2) - j
    if j >= len(s2):
        return len(s1) - i
    if dp[i][j] > 0:
        return dp[i][j]
    if s1[i] == s2[j]:
        return 1 + recurse(s1, s2, i + 1, j + 1, dp)
    c1 = 1 + recurse(s1, s2, i + 1, j, dp)
    c2 = 1 + recurse(s1, s2, i, j + 1, dp)
    dp[i][j] = min(c1, c2)
    return dp[i][j]
