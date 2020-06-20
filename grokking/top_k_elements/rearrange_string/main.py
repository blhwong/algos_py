"""
Problem Statement #
Given a string, find if its letters can be rearranged in such a way that no two same characters come next to each other.

Example 1:

Input: "aappp"
Output: "papap"
Explanation: In "papap", none of the repeating characters come next to each other.
Example 2:

Input: "Programming"
Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
Explanation: None of the repeating characters come next to each other.
Example 3:

Input: "aapa"
Output: ""
Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".
"""

from heapq import *


def rearrange_string(str):
    max_heap = []

    freq = {}

    for char in str:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1

    for char, count in freq.items():
        heappush(max_heap, (-count, char))

    ans = ''
    prev_char, prev_freq = None, 0
    while max_heap:
        count, char = heappop(max_heap)

        if prev_char and prev_freq > 0:
            heappush(max_heap, (-prev_freq, prev_char))
        ans += char
        prev_char = char
        prev_freq = -count - 1


    return ans if len(ans) == len(str) else ''

