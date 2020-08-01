def interweavingStrings(one, two, three):
    def solve(i, j):
        if len(one) + len(two) != len(three):
            return False
        k = i + j
        if k == len(three):
            return True

        if i < len(one) and one[i] == three[k]:
            if solve(i + 1, j):
                return True

        if j < len(two) and two[j] == three[k]:
            return solve(i, j + 1)

        return False

    return solve(0, 0)
