class Solution:
    def isPalindrome(self, s: str) -> bool:

        def get_palindrome_bounds(s, start_left, start_right):
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

        def clean(s):
            return ''.join([i for i in list(s.lower()) if i.isalnum()])


        cleaned = clean(s)

        if not cleaned:
            return True

        half = len(cleaned) // 2
        odd = len(cleaned) % 2 != 0
        if odd:
            left, right = get_palindrome_bounds(cleaned, half, half)
        else:
            left, right = get_palindrome_bounds(cleaned, half - 1, half)

        return right - left + 1 == len(cleaned)
