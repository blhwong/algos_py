"""
Problem Statement
Given a string, find the minimum number of characters that we can remove to make it a palindrome.

Example 1:

Input: "abdbca"
Output: 1
Explanation: By removing "c", we get a palindrome "abdba".
Example 2:

Input: = "cddpd"
Output: 2
Explanation: Deleting "cp", we get a palindrome "ddd".
Example 3:

Input: = "pqr"
Output: 2
Explanation: We have to remove any two characters to get a palindrome, e.g. if we
remove "pq", we get palindrome "r".
"""


def find_minimum_deletions(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = 1

    for start in range(len(s) - 1, -1, -1):
        for end in range(start + 1, len(s)):
            if s[start] == s[end]:
                dp[start][end] = dp[start + 1][end - 1] + 2
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    return len(s) - dp[0][-1]
