def searchInSortedMatrix(matrix, target):
    row, col = 0, len(matrix[0]) - 1
    ans = [-1, -1]

    while row >= 0 and col >= 0:
        val = matrix[row][col]
        if val == target:
            return [row, col]
        elif val < target:
            row += 1
        else:
            col -= 1

    return ans
