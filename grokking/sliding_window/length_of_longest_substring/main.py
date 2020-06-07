"""
Problem Statement
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:

Input: String = "aabccbb", k = 2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
Example 2:

Input: String = "abbcb", k = 1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
Example 3:

Input: String = "abccde", k = 1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".


aaaa
bbb
cccc

"""


def length_of_longest_substring(str, k):
    ans = 0
    start = 0
    tracker = {}
    curr_max = 0
    for end in range(len(str)):
        letter = str[end]

        if letter not in tracker:
            tracker[letter] = 0
        tracker[letter] += 1

        curr_max = max(curr_max, tracker[letter])

        if end - start + 1 - curr_max > k:
            left = str[start]
            tracker[left] -= 1
            start += 1


        ans = max(ans, end - start + 1)


    return ans
