class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = 0
        tracker = {}

        for end, char in enumerate(s):
            if char in tracker:
                start = max(start, tracker[char] + 1)

            tracker[char] = end

            ans = max(ans, end - start + 1)

        return ans
