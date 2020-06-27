class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        def find_palindrome_bounds(s, start_left, start_right):
            left = start_left
            right = start_right
            if s[left] != s[right]:
                return -1, -1
            while (
                left >= 0 and
                right < len(s) and
                s[left] == s[right]
            ):
                left -= 1
                right += 1
            return left + 1, right - 1


        left, right = 0, 0
        for i in range(len(s) - 1):
            l1, r1 = find_palindrome_bounds(s, i, i)
            l2, r2 = find_palindrome_bounds(s, i, i + 1)
            if r2 - l2 > right - left:
                left, right = l2, r2
            elif r1 - l1 > right - left:
                left, right = l1, r1

        return s[left:right + 1]
