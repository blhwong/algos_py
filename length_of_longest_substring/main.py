# Left and right pointers
# while right pointer is less than length of string
#     if letter at right pointer is in substring
#         increment left pointer until the letter at right pointer is out of substring
#     add letter at right pointer to substring
#     update max if needed
#     Increment right pointer

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left_idx = 0
        right_idx = 1
        ss = s[0]
        max_ss = ss
        while right_idx < len(s):
            if s[right_idx] in ss:
                while s[left_idx] != s[right_idx]:
                    left_idx += 1
                left_idx += 1
                ss = s[left_idx:right_idx]
            ss += s[right_idx]
            if len(ss) > len(max_ss):
                max_ss = ss
            right_idx += 1
        return len(max_ss)

