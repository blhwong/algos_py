"""
Problem Statement
Given a string, find the length of the longest substring which has no repeating characters.

Example 1:

Input: String = "aabccbb"
Output: 3
Explanation: The longest substring without any repeating characters is "abc".
Example 2:

Input: String = "abbbb"
Output: 2
Explanation: The longest substring without any repeating characters is "ab".
Example 3:

Input: String = "abccde"
Output: 3
Explanation: Longest substrings without any repeating characters are "abc" & "cde".
"""


def non_repeat_substring(str1):
    char_map = {}
    start = 0
    ans = 0
    for end in range(len(str1)):
        if str1[end] in char_map:
            start = max(start, char_map[str1[end]] + 1)
        char_map[str1[end]] = end
        ans = max(ans, end - start + 1)
    return ans
