"""
Problem Statement
Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

Example 1:

Input: "t o m o r r o w"
Output: 2
Explanation: The longest repeating subsequence is "or" {tomorrow}.

Example 2:

Input: "a a b d b c e c"
Output: 3
Explanation: The longest repeating subsequence is "a b c" {a a b d b c e c}.

Example 3:

Input: "f m f f"
Output: 2
Explanation: The longest repeating subsequence is "f f" {f m f f, f m f f}. Please note the second last character is shared in LRS.
"""


def find_lrs_length_iterative(s):
    dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]

    for i in range(1, len(s) + 1):
        for j in range(1, len(s) + 1):
            if s[i - 1] == s[j - 1] and i < j:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[-1][-1]


def find_lrs_length_recursive(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    return recurse(s, 0, 0, dp)


def recurse(s, i, j, dp):
    if i >= len(s):
        return 0
    if j >= len(s):
        return 0
    if dp[i][j] > 0:
        return dp[i][j]
    if s[i] == s[j] and i < j:
        dp[i][j] = 1 + recurse(s, i + 1, j + 1, dp)
        return dp[i][j]
    c1 = recurse(s, i + 1, j, dp)
    c2 = recurse(s, i, j + 1, dp)
    dp[i][j] = max(c1, c2)
    return dp[i][j]
