class Trie:
    def __init__(self):
        self.storage = {}
        self.end_symbol = '*'

    def add(self, word):
        ref = self.storage
        for char in word:
            if char not in ref:
                ref[char] = {}
            ref = ref[char]
        ref[self.end_symbol] = word

def boggleBoard(board, words):
    def visit(row, col, curr_trie, trie, visited, ans):
        if trie.end_symbol in curr_trie:
            word = curr_trie[trie.end_symbol]
            ans.add(word)

        if not (0 <= row < len(board) and 0 <= col < len(board[0])):
            return
        if visited[row][col]:
            return
        char = board[row][col]
        if char not in curr_trie:
            return

        visited[row][col] = True
        visit(row - 1, col - 1, curr_trie[char], trie, visited, ans)
        visit(row - 1, col, curr_trie[char], trie, visited, ans)
        visit(row - 1, col + 1, curr_trie[char], trie, visited, ans)
        visit(row , col + 1, curr_trie[char], trie, visited, ans)
        visit(row + 1, col + 1, curr_trie[char], trie, visited, ans)
        visit(row + 1, col, curr_trie[char], trie, visited, ans)
        visit(row + 1, col - 1, curr_trie[char], trie, visited, ans)
        visit(row, col - 1, curr_trie[char], trie, visited, ans)
        visited[row][col] = False

    ans = set()
    trie = Trie()
    for word in words:
        trie.add(word)

    visited = [[False] * len(board[0]) for _ in board]
    for row in range(len(board)):
        for col in range(len(board[0])):
            visit(row, col, trie.storage, trie, visited, ans)

    return list(ans)
