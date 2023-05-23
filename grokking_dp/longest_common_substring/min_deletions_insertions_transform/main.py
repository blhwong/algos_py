"""
Problem Statement
Given strings s1 and s2, we need to transform s1 into s2 by deleting and inserting characters. Write a function to calculate the count of the minimum number of deletion and insertion operations.

Example 1:

Input: s1 = "abc"
       s2 = "fbc"
Output: 1 deletion and 1 insertion.
Explanation: We need to delete {'a'} and insert {'f'} to s1 to transform it into s2.
Example 2:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2 deletions and 1 insertion.
Explanation: We need to delete {'a', 'c'} and insert {'c'} to s1 to transform it into s2.
Example 3:

Input: s1 = "passport"
       s2 = "ppsspt"
Output: 3 deletions and 1 insertion
Explanation: We need to delete {'a', 'o', 'r'} and insert {'p'} to s1 to transform it into s2.
"""


def find_mdi(s1, s2):
    dp = [[0] * len(s1) for _ in range(len(s2))]

    for i in range(len(s2)):
        dp[i][0] = 1 if s1[0] == s2[i] else 0

    for j in range(len(s1)):
        dp[0][j] = 1 if s1[j] == s2[0] else 0

    for i in range(1, len(s2)):
        for j in range(1, len(s1)):
            if s2[i] == s1[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    longest_common_subsequence = dp[-1][-1]
    deletions = len(s1) - longest_common_subsequence
    insertions = len(s2) - longest_common_subsequence

    return deletions, insertions
