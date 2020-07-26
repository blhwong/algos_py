def boggleBoard(board, words):
    def visit(row, col, word, start, visited):
        if start == len(word):
            return True
        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            return False
        if visited[row][col]:
            return False
        if board[row][col] != word[start]:
            return False

        visited[row][col] = True
        return (
            visit(row , col + 1, word, start + 1, visited) or
            visit(row + 1, col, word, start + 1, visited) or
            visit(row - 1, col, word, start + 1, visited) or
            visit(row, col - 1, word, start + 1, visited) or
            visit(row + 1, col + 1, word, start + 1, visited) or
            visit(row + 1, col - 1, word, start + 1, visited) or
            visit(row - 1, col - 1, word, start + 1, visited) or
            visit(row - 1, col + 1, word, start + 1, visited)
        )

    ans = []
    for word in words:
        found = False
        for row in range(len(board)):
            if found:
                break
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited = [[False] * len(board[0]) for _ in board]
                    found = visit(row, col, word, 0, visited)
                    if found:
                        ans.append(word)
                        break

    return ans
