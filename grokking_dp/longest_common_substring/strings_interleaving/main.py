"""
Problem Statement
Given three strings 'm', 'n', and 'p', write a method to find out if 'p' has been formed by interleaving 'm' and 'n'. 'p' would be considered interleaving 'm' and 'n' if it contains all the letters from 'm' and 'n' and the order of letters is preserved too.

Example 1:

Input: m="abd", n="cef", p="abcdef"
Output: true
Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.
Example 2:

Input: m="abd", n="cef", p="adcbef"
Output: false
Explanation: 'p' contains all the letters from 'm' and 'n' but does not preserve the order.
Example 3:

Input: m="abc", n="def", p="abdccf"
Output: false
Explanation: 'p' does not contain all the letters from 'm' and 'n'.
Example 4:

Input: m="abcdef", n="mnop", p="mnaobcdepf"
Output: true
Explanation: 'p' contains all the letters from 'm' and 'n' and preserves their order too.
"""


def find_si(m, n, p):
    dp = [[[None] * (len(p) + 1) for _ in range(len(n) + 1)] for _ in range(len(m) + 1)]
    return recurse(m, n, p, 0, 0, 0, dp)


def recurse(m, n, p, i, j, k, dp):
    if k >= len(p) and j >= len(n) and i >= len(m):
        return True

    if k >= len(p):
        return False

    if dp[i][j][k] is not None:
        return dp[i][j][k]

    c1, c2 = False, False
    if i < len(m) and m[i] == p[k]:
        c1 = recurse(m, n, p, i + 1, j, k + 1, dp)
    if j < len(n) and n[j] == p[k]:
        c2 = recurse(m, n, p, i, j + 1, k + 1, dp)

    dp[i][j][k] = c1 or c2

    return dp[i][j][k]
