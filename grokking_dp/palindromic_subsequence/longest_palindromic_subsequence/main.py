"""
Problem Statement
Given a sequence, find the length of its Longest Palindromic Subsequence (LPS). In a palindromic subsequence, elements read the same backward and forward.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: "abdbca"
Output: 5
Explanation: LPS is "abdba".
Example 2:

Input: = "cddpd"
Output: 3
Explanation: LPS is "ddd".
Example 3:

Input: = "pqr"
Output: 1
Explanation: LPS could be "p", "q" or "r".
"""


def find_lps_length_iterative(s):
    dp = [[0] * len(s) for _ in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = 1

    for start in range(len(s) - 1, -1, -1):
        for end in range(start + 1, len(s)):
            if s[start] == s[end]:
                dp[start][end] = 2 + dp[start + 1][end - 1]
            else:
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    return dp[0][-1]


def find_lps_length_recursive(s):
    dp = [[-1] * len(s) for _ in range(len(s))]
    return recurse(s, 0, len(s) - 1, dp)


def recurse(s, left, right, dp):
    if right < left:
        return 0

    if dp[left][right] > -1:
        return dp[left][right]

    if left == right:
        return 1

    if s[left] == s[right]:
        dp[left][right] = 2 + recurse(s, left + 1, right - 1, dp)
        return dp[left][right]

    one = recurse(s, left + 1, right, dp)
    two = recurse(s, left, right - 1, dp)

    dp[left][right] = max(one, two)

    return dp[left][right]


def find_lps_length(s):
    subsequences = set()
    for i in range(len(s)):
        for j in range(len(s)):
            subsequences.add(s[0:i] + s[i + j + 1:])

    ans = 1

    for sub in subsequences:
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
