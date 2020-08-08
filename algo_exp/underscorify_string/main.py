def get_locations(string, substring):
    intervals = []

    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            intervals.append([i, i + len(substring)])

    merged = []

    start, end = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] > end:
            merged.append([start, end])
            start, end = curr
        else:
            end = max(end, curr[1])

    merged.append([start, end])

    return [i for sublist in merged for i in sublist]


def underscorifySubstring(string, substring):
    if substring not in string:
        return string

    locations = get_locations(string, substring)

    j = 0
    ans = ''
    for i in range(len(string)):
        if j < len(locations) and i == locations[j]:
            ans += '_'
            j += 1
        ans += string[i]

    if j < len(locations):
        ans += '_'

    return ans
