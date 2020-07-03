class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        start = 0
        tracker = {}
        curr_longest = 0
        for end in range(len(s)):
            letter = s[end]
            if letter not in tracker:
                tracker[letter] = 0

            tracker[letter] += 1

            curr_longest = max(curr_longest, tracker[letter]) # current longest string

            if end - start + 1 - curr_longest > k: # window - current longest string = characters replaced
                left = s[start]
                tracker[left] -= 1
                start += 1

            ans = max(ans, end - start + 1)

        return ans
