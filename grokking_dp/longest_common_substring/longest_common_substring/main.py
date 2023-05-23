"""
Problem Statement
Given two strings 's1' and 's2', find the length of the longest substring which is common in both the strings.

Example 1:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: The longest common substring is "bd".
Example 2:

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 3
Explanation: The longest common substring is "ssp".
"""


def find_lcs_length(s1, s2):
    dp = [[0] * len(s1) for _ in range(len(s2))]
    ans = 0

    for i in range(len(s2)):
        dp[i][0] = 1 if s1[0] == s2[i] else 0
        ans = max(ans, dp[i][0])

    for j in range(len(s1)):
        dp[0][j] = 1 if s1[j] == s2[0] else 0
        ans = max(ans, dp[0][j])

    for i in range(1, len(s2)):
        for j in range(1, len(s1)):
            if s1[j] == s2[i]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                ans = max(ans, dp[i][j])

    return ans
