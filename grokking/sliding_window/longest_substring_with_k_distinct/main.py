"""
Problem Statement #
Given a string, find the length of the longest substring in it with no more than K distinct characters.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".

Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".

Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".
"""

def longest_substring_with_k_distinct(str1, k):
    ans = 0
    chars = {}
    start = 0

    for end in range(len(str1)):
        if str1[end] not in chars:
            chars[str1[end]] = 0
        chars[str1[end]] += 1

        while len(chars) > k:
            chars[str1[start]] -= 1
            if chars[str1[start]] == 0:
                del chars[str1[start]]
            start += 1

        ans = max(ans, end - start + 1)

    return ans
