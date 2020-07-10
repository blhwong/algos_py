def isValidSubsequence(array, sequence):
    i = 0

    for num in array:
        if i < len(sequence) and num == sequence[i]:
            i += 1

    return i == len(sequence)
