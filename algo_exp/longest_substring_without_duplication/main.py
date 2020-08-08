def longestSubstringWithoutDuplication(string):
    start = 0
    ans = ''
    tracker = {}
    for end in range(len(string)):
        curr = string[end]
        if curr in tracker:
            start = max(start, tracker[curr] + 1)

        tracker[curr] = end

        ans = max(ans, string[start:end + 1], key = lambda x: len(x))

    return ans
