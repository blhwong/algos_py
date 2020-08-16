def get_char_counts(string):
    tracker = {}
    for char in string:
        if char not in tracker:
            tracker[char] = 0
        tracker[char] += 1

    return tracker


def smallestSubstringContaining(bigString, smallString):
    target_table = get_char_counts(smallString)
    curr = {}
    left = 0
    size = float('inf')
    left_bound, right_bound = None, None
    count = 0
    for right, char in enumerate(bigString):
        char = bigString[right]
        if char in target_table:
            if char not in curr:
                curr[char] = 0
            curr[char] += 1
            if curr[char] == target_table[char]:
                count += 1
            while count == len(target_table):
                if right - left + 1 < size:
                    left_bound = left
                    right_bound = right
                    size = right - left + 1

                left_char = bigString[left]
                if left_char in curr:
                    curr[left_char] -= 1
                    if curr[left_char] < target_table[left_char]:
                        count -= 1
                left += 1

    return bigString[left_bound:right_bound + 1] if size != float('inf') else ''
