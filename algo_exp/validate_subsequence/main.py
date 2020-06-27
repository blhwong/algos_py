def isValidSubsequence(array, sequence):
    i, j = 0, 0

    while i < len(array):
        if j < len(sequence) and array[i] == sequence[j]:
            j += 1
        i += 1

    return j == len(sequence)
