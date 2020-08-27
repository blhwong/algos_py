def longestSubstringWithoutDuplication(string):
    start = 0
    ans = ''
    tracker = {}
    for end, char in enumerate(string):
        if char in tracker:
            start = max(start, tracker[char] + 1)
        tracker[char] = end
        ans = max(ans, string[start:end + 1], key=len)

    return ans
