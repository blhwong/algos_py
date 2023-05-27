"""
Problem Statement
Given strings s1 and s2, we need to transform s1 into s2 by deleting, inserting, or replacing characters. Write a function to calculate the count of the minimum number of edit operations.

Example 1:

Input: s1 = "bat"
       s2 = "but"
Output: 1
Explanation: We just need to replace 'a' with 'u' to transform s1 to s2.
Example 2:

Input: s1 = "abdca"
       s2 = "cbda"
Output: 2
Explanation: We can replace first 'a' with 'c' and delete second 'c'.
Example 3:

Input: s1 = "passpot"
       s2 = "ppsspqrt"
Output: 3
Explanation: Replace 'a' with 'p', 'o' with 'q', and insert 'r'.

"""


def find_min_operations_iterative(s1, s2):
    dp = [[0] * (len(s2) + 1) for _ in range(len(s1) + 1)]

    for i in range(len(s1) + 1):
        dp[i][0] = i

    for j in range(len(s2) + 1):
        dp[0][j] = j

    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j - 1],        # replace
                    min(dp[i - 1][j],        # delete
                        dp[i][j - 1]))       # insert

    return dp[-1][-1]


def find_min_operations_recursive(s1, s2):
    dp = [[-1] * len(s2) for _ in range(len(s1))]
    return recurse(s1, s2, 0, 0, dp)


def recurse(s1, s2, i, j, dp):
    if i >= len(s1):
        return 0
    if j >= len(s2):
        return 0

    if dp[i][j] > -1:
        return dp[i][j]

    if s1[i] == s2[j]:
        return recurse(s1, s2, i + 1, j + 1, dp)

    replace = recurse(s1, s2, i + 1, j + 1, dp)
    insert = recurse(s1, s2, i, j + 1, dp)
    delete = recurse(s1, s2, i + 1, j, dp)

    dp[i][j] = 1 + min(replace, min(insert, delete))
    return dp[i][j]
