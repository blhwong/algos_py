from typing import List

class Trie:
    def __init__(self):
        self.root = {}
        self.end_symbol = '*'

    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

        curr[self.end_symbol] = True

    def search(self, word):
        curr = self.root
        for char in word:
            if char not in curr:
                return False
            curr = curr[char]

        return self.end_symbol in curr

class Solution:
    def dfs(self, board, trie, end_symbol, visited, row, col, string, ans):
        if end_symbol in trie and trie[end_symbol]:
            ans.append(string)
            trie[end_symbol] = False
        if not 0 <= row < len(board):
            return
        if not 0 <= col < len(board[0]):
            return
        if (row, col) in visited:
            return
        char = board[row][col]
        if char not in trie:
            return

        copy = visited.copy()
        copy.add((row, col))

        self.dfs(board, trie[char], end_symbol, copy, row + 1, col, string + char, ans)
        self.dfs(board, trie[char], end_symbol, copy, row, col + 1, string + char, ans)
        self.dfs(board, trie[char], end_symbol, copy, row - 1, col, string + char, ans)
        self.dfs(board, trie[char], end_symbol, copy, row, col - 1, string + char, ans)


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)

        ans = []

        for row in range(len(board)):
            for col in range(len(board[0])):
                self.dfs(board, trie.root, trie.end_symbol, set(), row, col, '', ans)

        return ans
