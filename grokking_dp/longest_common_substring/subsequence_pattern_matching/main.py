"""
Subsequence Pattern Matching
Problem Statement
Given a string and a pattern, write a method to count the number of times the pattern appears in the string as a subsequence.

Example 1: Input: string: "baxmx", pattern: "ax"
Output: 2
Explanation: {baxmx, baxmx}.

Example 2:

Input: string: "tomorrow", pattern: "tor"
Output: 4
Explanation: Following are the four occurences: {tomorrow, tomorrow, tomorrow, tomorrow}.
"""


def find_spm_count_iterative(s, p):
    dp = [[0] * (len(p) + 1) for _ in range(len(s) + 1)]

    for i in range(len(s) + 1):
        dp[i][0] = 1

    for i in range(1, len(s) + 1):
        for j in range(1, len(p) + 1):
            c1 = 0
            if s[i - 1] == p[j - 1]:
                c1 = dp[i - 1][j - 1]
            c2 = dp[i - 1][j]
            dp[i][j] = c1 + c2

    return dp[-1][-1]


def find_spm_count_recursive(s, p):
    dp = [[-1] * len(p) for _ in range(len(s))]
    return recurse(s, p, 0, 0, dp)


def recurse(s, p, i, j, dp):
    if j >= len(p):
        return 1
    if i >= len(s):
        return 0
    if dp[i][j] > -1:
        return dp[i][j]
    c1 = 0
    if s[i] == p[j]:
        c1 = recurse(s, p, i + 1, j + 1, dp)
    c2 = recurse(s, p, i + 1, j, dp)
    dp[i][j] = c1 + c2
    return dp[i][j]
