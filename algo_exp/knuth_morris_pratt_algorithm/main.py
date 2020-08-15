def get_pattern(substring):
    pattern = [-1] * len(substring)
    j, i = 0, 1
    while i < len(substring):
        if substring[i] == substring[j]:
            pattern[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1

    return pattern


def knuthMorrisPrattAlgorithm(string, substring):
    pattern = get_pattern(substring)
    i, j = 0, 0
    while i < len(string) and j < len(substring):
        if string[i] == substring[j]:
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j - 1] + 1
        else:
            i += 1

    return j == len(substring)
