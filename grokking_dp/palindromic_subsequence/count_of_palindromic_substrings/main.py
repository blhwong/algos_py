"""
Problem Statement
Given a string, find the total number of palindromic substrings in it. Please note we need to find the total number of substrings and not subsequences.

Example 1:

Input: "abdbca"
Output: 7
Explanation: Here are the palindromic substrings, "a", "b", "d", "b", "c", "a", "bdb".
Example 2:

Input: = "cddpd"
Output: 7
Explanation: Here are the palindromic substrings, "c", "d", "d", "p", "d", "dd", "dpd".
Example 3:

Input: = "pqr"
Output: 3
Explanation: Here are the palindromic substrings,"p", "q", "r".
"""


def count_palindromic_substrings_iterative(s):
    dp = [[False] * len(s) for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = True

    ans = len(s)

    for start in range(len(s) - 1, -1, -1):
        for end in range(start + 1, len(s)):
            if s[start] == s[end]:
                if dp[start + 1][end - 1] or end - start == 1:
                    dp[start][end] = True
                    ans += 1

    return ans


def count_palindromic_substrings_recursive(s):
    pass


def count_palindromic_substrings(s):
    ans = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_palindrome(s[i:j]):
                ans += 1

    return ans


def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True
