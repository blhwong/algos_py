def riverSizes(matrix):
    visited = [[False] * len(matrix[0]) for _ in matrix]

    def get_size(row, col):
        if visited[row][col]:
            return 0

        size = 1
        visited[row][col] = True

        j = col + 1
        while j < len(matrix[0]) and matrix[row][j] == 1:
            size += get_size(row, j)
            j += 1

        j = col - 1
        while j >= 0 and matrix[row][j] == 1:
            size += get_size(row, j)
            j -= 1

        i = row + 1
        while i < len(matrix) and matrix[i][col] == 1:
            size += get_size(i, col)
            i += 1

        i = row - 1
        while i >= 0 and matrix[i][col] == 1:
            size += get_size(i, col)
            i -= 1

        return size


    ans = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] and not visited[row][col]:
                ans.append(get_size(row, col))

    return ans
