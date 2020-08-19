def longestPalindromicSubstring(string):
    if not string:
        return ''

    def get_palindrome_bounds(i, j):
        while i >= 0 and j < len(string) and string[i] == string[j]:
            i -= 1
            j += 1

        return i + 1, j - 1

    left, right = 0, 0

    for i in range(len(string) - 1):
        l1, r1 = get_palindrome_bounds(i, i)
        l2, r2 = get_palindrome_bounds(i, i + 1)
        if r2 - l2 > right - left:
            left, right = l2, r2
        elif r1 - l1 > right - left:
            left, right = l1, r1

    return string[left:right + 1]
