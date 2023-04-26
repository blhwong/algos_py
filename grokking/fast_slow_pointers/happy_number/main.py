"""
Problem Statement #
Any number will be called a happy number if, after repeatedly replacing it with a number equal to the sum of the square of all of its digits, leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a cycle of numbers which does not include ‘1’.

Example 1:

Input: 23
Output: true (23 is a happy number)
Example 2:

Input: 12
Output: false (12 is not a happy number)
"""


def find_happy_number(num):
    slow, fast = num, num

    while fast != 1:
        slow = calculate(slow)
        fast = calculate(calculate(fast))
        if slow == fast:
            return False

    return True


def calculate(num):
    ans = 0
    for s in str(num):
        ans += int(s) ** 2
    return ans
