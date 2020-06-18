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
    result = []
    q = deque()
    q.append(['', num, num])
    while q:
        str, open_left, closed_left = q.popleft()
        if len(str) == num * 2:
            result.append(str)
        else:
            if open_left > 0:
                q.append([str + '(', open_left - 1, closed_left])

            if closed_left > open_left:
                q.append([str + ')', open_left, closed_left - 1])

    return result


def generate_valid_parentheses_recursive(num):
    result = []
    def generate(curr, open_left, closed_left):
        if open_left < 0 or closed_left < 0:
            return
        if closed_left < open_left:
            return
        if len(curr) == num * 2:
            result.append(curr)
            return

        generate(curr + '(', open_left -1, closed_left)
        generate(curr + ')', open_left, closed_left - 1)

    generate('', num, num)
    return result
