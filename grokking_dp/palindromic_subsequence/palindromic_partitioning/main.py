"""
Problem Statement
Given a string, we want to cut it into pieces such that each piece is a palindrome. Write a function to return the minimum number of cuts needed.

Example 1:

Input: "abdbca"
Output: 3
Explanation: Palindrome pieces are "a", "bdb", "c", "a".
Example 2:

Input: = "cddpd"
Output: 2
Explanation: Palindrome pieces are "c", "d", "dpd".
Example 3:

Input: = "pqr"
Output: 2
Explanation: Palindrome pieces are "p", "q", "r".
Example 4:

Input: = "pp"
Output: 0
Explanation: We do not need to cut, as "pp" is a palindrome.
"""


def find_mpp_cuts(s):
    dp = [[False] * len(s) for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = True

    for start in range(len(s) - 1, -1, -1):
        for end in range(start + 1, len(s)):
            if s[start] == s[end]:
                if dp[start + 1][end - 1] or end - start == 1:
                    dp[start][end] = True

    cuts = [0 for _ in range(len(s))]

    for start in range(len(s) - 1, -1, -1):
        min_cuts = len(s)
        for end in range(len(s) - 1, start - 1, -1):
            if dp[start][end]:
                min_cuts = 0 if end == len(s) - 1 else min(min_cuts, 1 + cuts[end + 1])

        cuts[start] = min_cuts

    return cuts[0]
