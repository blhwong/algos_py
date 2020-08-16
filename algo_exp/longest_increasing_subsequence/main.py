"""
            5
      -24        7
          2    5    12
            3   6  10  12
                            35
"""
def longestIncreasingSubsequenceBruteForce(array):
    def solve(start, curr_sequence):
        if start >= len(array):
            return curr_sequence

        ans = curr_sequence
        for i in range(start, len(array)):
            num = array[i]
            if not curr_sequence or num > curr_sequence[-1]:
                ans = max(ans, solve(i + 1, curr_sequence + [num]), key=len)

        return ans


    return solve(0, [])


def longestIncreasingSubsequenceDP(array):
    lengths = [1] * len(array)
    sequences = [None] * len(array)

    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j

    ans = []

    largest_sequence = max(enumerate(lengths), key=lambda x: x[1])
    curr_idx, _ = largest_sequence
    while curr_idx is not None:
        ans.append(array[curr_idx])
        curr_idx = sequences[curr_idx]

    return list(reversed(ans))


def longestIncreasingSubsequence(array):
    pass
