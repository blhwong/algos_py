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

def squareOfZeroesBruceForce(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            is_square = get_is_square(matrix, row, col)
            if is_square:
                return True

    return False

def squareOfZeroes(matrix):
    dp = [[(0, 0)] * len(matrix) for _ in matrix]

    for row in reversed(range(len(matrix))):
        for col in reversed(range(len(matrix))):
            zeroes_below, zeroes_right = 0, 0
            if col < len(matrix) - 1:
                _, right = dp[row][col + 1]
                zeroes_right += right
            if row < len(matrix) - 1:
                below, _ = dp[row + 1][col]
                zeroes_below += below
            if matrix[row][col] == 0:
                zeroes_below += 1
                zeroes_right += 1
            dp[row][col] = (zeroes_below, zeroes_right)

    for row in range(len(matrix)):
        for col in range(len(matrix)):
            size = min(dp[row][col])
            if size > 1 and row + size - 1 < len(matrix):
                top_right_zeroes_below, _ = dp[row][col + size - 1]
                _, bottom_left_zeroes_right = dp[row + size - 1][col]
                bottom_right_zeroes_below, bottom_right_zeroes_right = dp[row + size - 1][col + size - 1]
                if (
                    top_right_zeroes_below == size and
                    bottom_left_zeroes_right == size and
                    top_right_zeroes_below - bottom_right_zeroes_below + 1 >= size and
                    bottom_left_zeroes_right - bottom_right_zeroes_right + 1 >= size
                ):
                    return True


    return False
