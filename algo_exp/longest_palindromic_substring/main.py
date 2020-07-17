def longestPalindromicSubstring(string):
    if not string:
        return ''

    def longest_palindrome(i, j):
        count = 0
        while i - count >= 0 and j + count < len(string):
            if string[i - count] != string[j + count]:
                break
            count += 1
        left = i - count + 1
        right = j + count
        return string[left:right]

    ans = string[0]
    for i in range(len(string) - 1):
        one, two = longest_palindrome(i, i), longest_palindrome(i, i + 1)
        if len(one) > len(ans):
            ans = one
        if len(two) > len(ans):
            ans = two

    return ans

