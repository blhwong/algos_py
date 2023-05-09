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


def rearrange_string(s):
    freq_map = {}
    max_heap = []
    ans = ''

    for char in s:
        if char not in freq_map:
            freq_map[char] = 0
        freq_map[char] += 1

    for char, freq in freq_map.items():
        heappush(max_heap, (-freq, char))

    prev, prev_freq = None, 0
    while len(max_heap) > 0:
        freq, char = heappop(max_heap)
        if -prev_freq > 1:
            heappush(max_heap, (prev_freq + 1, prev))
        ans += char
        prev = char
        prev_freq = freq

    return ans if len(ans) == len(s) else ''
