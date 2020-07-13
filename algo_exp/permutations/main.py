def getPermutations(array):
    if not array:
        return []

    ans = [[]]

    for num in array:
        tmp = []
        for subset in ans:
            for i in range(len(subset) + 1):
                tmp.append(subset[:i] + [num] + subset[i:])

        ans = tmp

    return ans
