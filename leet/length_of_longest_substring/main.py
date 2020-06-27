class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        start = 0
        tracker = {}

        for end in range(len(s)):
            letter = s[end]

            if letter in tracker:
                start = max(start, tracker[letter] + 1)

            tracker[letter] = end

            ans = max(ans, end - start + 1)

        return ans
