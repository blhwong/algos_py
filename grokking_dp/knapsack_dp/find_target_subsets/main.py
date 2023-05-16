"""
Problem Statement
Given a set of positive numbers (non zero) and a target sum 'S'. Each number should be assigned either a '+' or '-' sign. We need to find out total ways to assign symbols to make the sum of numbers equal to target 'S'.

Example 1:
Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': {+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}
Example 2:
Input: {1, 2, 7, 1}, S=9
Output: 2
Explanation: The given set has '2' ways to make a sum of '9': {+1+2+7-1} & {-1+2+7+1}
"""

def find_target_subsets_recursive(num, s):
    return recurse(num, s, 0)

def recurse(num, curr_sum, i):
    if i >= len(num):
        return 1 if curr_sum == 0 else 0
    positive = recurse(num, curr_sum + num[i], i + 1)
    negative = recurse(num, curr_sum - num[i], i + 1)
    return positive + negative


def find_target_subsets_iterative(num, s):
    total_sum = sum(num)
    if (s + total_sum) % 2 != 0:
        return 0
    return count_subsets(num, (s + total_sum) // 2)

def count_subsets(num, s):
    dp = [[0] * (s + 1) for _ in range(len(num))]

    for i in range(len(num)):
        dp[i][0] = 1

    for j in range(1, s + 1):
        dp[0][j] = 1 if num[0] == j else 0

    for i in range(1, len(num)):
        for j in range(1, s + 1):
            one = 0
            if num[i] <= j:
                one = dp[i - 1][j - num[i]]
            two = dp[i - 1][j]
            dp[i][j] = one + two

    return dp[-1][s]
