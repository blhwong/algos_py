"""
Problem Statement
Given a string, find the length of its Longest Palindromic Substring (LPS). In a palindromic string, elements read the same backward and forward.

Example 1:

Input: "abdbca"
Output: 3
Explanation: LPS is "bdb".
Example 2:

Input: = "cddpd"
Output: 3
Explanation: LPS is "dpd".
Example 3:

Input: = "pqr"
Output: 1
Explanation: LPS could be "p", "q" or "r".
"""


def find_lps_length_iterative(s):
    dp = [[False] * len(s) for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = True

    ans = 1

    for start in range(len(s)):
        for end in range(start + 1, len(s)):
            if s[start] == s[end]:
                if dp[start + 1][end - 1] or end - start == 1:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                    ans = max(ans, dp[start][end])

    return ans


def find_lps_length_recursive(s):
    dp = [[0] * len(s) for _ in range(len(s))]
    return recurse(s, 0, len(s) - 1, dp)


def recurse(s, left, right, dp):
    if left > right:
        return 0
    if left == right:
        return 1

    if dp[left][right] > 0:
        return dp[left][right]

    if s[left] == s[right]:
        remaining = right - left - 1
        if remaining == recurse(s, left + 1, right - 1, dp):
            return remaining + 2

    one = recurse(s, left + 1, right, dp)
    two = recurse(s, left, right - 1, dp)

    dp[left][right] = max(one, two)

    return dp[left][right]


def find_lps_length(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            substrings.add(s[i:j])

    ans = 1
    for sub in substrings:
        if is_palindrome(sub):
            ans = max(ans, len(sub))

    return ans


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
