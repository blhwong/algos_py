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

def build_from_sequences(array, sequences, start_idx):
    curr = start_idx
    ans = []
    while curr is not None:
        ans.append(array[curr])
        curr = sequences[curr]

    return list(reversed(ans))

def longestIncreasingSubsequenceDP(array):
    lengths = [1] * len(array)
    sequences = [None] * len(array)

    for i in range(len(array)):
        for j in range(i):
            if array[j] < array[i] and lengths[j] + 1 > lengths[i]:
                lengths[i] = lengths[j] + 1
                sequences[i] = j

    start, _ = max(enumerate(lengths), key = lambda x: x[1])
    return build_from_sequences(array, sequences, start)


def binary_search(left, right, indices, array, num):
    while left <= right:
        mid = (left + right) // 2
        if array[indices[mid]] < num:
            left = mid + 1
        else:
            right = mid - 1

    return left


def longestIncreasingSubsequence(array):
    length = 0
    sequences = [None] * len(array)
    indices = [None] * (len(array) + 1)

    for i, num in enumerate(array):
        new_length = binary_search(1, length, indices, array, num)
        sequences[i] = indices[new_length - 1]
        indices[new_length] = i
        length = max(length, new_length)

    return build_from_sequences(array, sequences, indices[length])
