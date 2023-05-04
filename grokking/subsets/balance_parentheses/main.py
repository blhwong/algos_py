"""
Problem Statement #
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example 1:

Input: N=2
Output: (()), ()()
Example 2:

Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

from collections import deque

def generate_valid_parentheses(num):
    ans = []
    q = deque()
    q.append(('', 0, 0))
    while q:
        curr, left, right = q.popleft()
        if len(curr) / 2 == num:
            ans.append(curr)
        if left < num:
            q.append((curr + '(', left + 1, right))
        if right < num and right < left:
            q.append((curr + ')', left, right + 1))

    return ans


def generate_valid_parentheses_recursive(num):
    return recurse(num, '', 0, 0, [])

def recurse(num, curr, left, right, ans):
    if len(curr) / 2 == num:
        ans.append(curr)
        return

    if left < num:
        recurse(num, curr + '(', left + 1, right, ans)

    if right < num and right < left:
        recurse(num, curr + ')', left, right + 1, ans)

    return ans
