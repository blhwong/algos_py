"""
Problem Statement
Given an array of positive numbers, where each element represents the max number of jumps that can be made forward from that element, write a program to find the minimum number of jumps needed to reach the end of the array (starting from the first element). If an element is 0, then we cannot move through that element.

Example 1:

Input = {2,1,1,1,4}
Output = 3
Explanation: Starting from index '0', we can reach the last index through: 0->2->3->4
Example 2:

Input = {1,1,3,6,9,3,0,1,3}
Output = 4
Explanation: Starting from index '0', we can reach the last index through: 0->1->2->3->8
"""


def count_min_jumps_iterative(jumps):
    n = len(jumps)
    dp = [float('infinity')] * n
    dp[0] = 0

    for start in range(n - 1):
        for end in range(start + 1, min(n, start + jumps[start] + 1)):
            dp[end] = min(dp[end], dp[start] + 1)

    return dp[n - 1]


def count_min_jumps_recursive(jumps):
    dp = [float('infinity')] * (len(jumps))
    return recurse(jumps, 0, dp)


def recurse(jumps, i, dp):
    if i >= len(jumps) - 1:
        return 0
    if dp[i] != float('infinity'):
        return dp[i]

    if jumps[i] == 0:
        return float('infinity')

    min_jumps = float('infinity')
    for jump in range(1, jumps[i] + 1):
        min_jumps = min(min_jumps, 1 + recurse(jumps, i + jump, dp))

    dp[i] = min_jumps
    return dp[i]
