"""
Problem Statement #
Given a string, sort it based on the decreasing frequency of its characters.

Example 1:

Input: "Programming"
Output: "rrggmmPiano"
Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
Example 2:

Input: "abcbab"
Output: "bbbaac"
Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
"""

from heapq import *

def sort_character_by_frequency(str):
    ans = ''

    max_heap = []
    freq_map = {}

    for char in str:
        if char not in freq_map:
            freq_map[char] = 0
        freq_map[char] += 1

    for k, v in freq_map.items():
        heappush(max_heap, (-v, k))

    while max_heap:
        freq, char = heappop(max_heap)
        ans += char * -freq

    return ans
