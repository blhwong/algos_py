def hasSingleCycle(array):
    i = 0
    visited = 0
    while visited < len(array):
        if i == 0 and visited > 0:
            return False
        i = ((i + array[i]) % len(array))
        visited += 1

    return i == 0
