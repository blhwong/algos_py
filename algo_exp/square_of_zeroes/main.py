def get_is_square(matrix, row, col):
    found = False
    for i in range(1, min(len(matrix) - row, len(matrix) - col)):
        found = True
        for j in range(i + 1):
            top = matrix[row][col + j]
            left = matrix[row + j][col]
            bottom = matrix[row + i][col + i - j]
            right = matrix[row + i - j][col + i]
            if top != 0 or right != 0 or bottom != 0 or left != 0:
                found = False
                break

        if found:
            return True

    return found

def squareOfZeroes(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            is_square = get_is_square(matrix, row, col)
            if is_square:
                return True

    return False
