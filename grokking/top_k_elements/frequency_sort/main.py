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
    freq = {}
    for char in str:
        if char not in freq:
            freq[char] = 0
        freq[char] += 1

    max_heap = []
    for char, count in freq.items():
        heappush(max_heap, (-count, char))

    while max_heap:
        count, char = heappop(max_heap)

        ans += ''.join([char] * -count)

    return ans
