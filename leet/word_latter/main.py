from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        all_combos = {}
        for word in wordList:
            for i in range(len(beginWord)):
                key = word[0:i] + '*' + word[i + 1:]
                if key not in all_combos:
                    all_combos[key] = []
                all_combos[key].append(word)

        q = deque()
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while q:
            word, level = q.popleft()
            for i in range(len(beginWord)):
                key = word[0:i] + '*' + word[i + 1:]
                if key not in all_combos:
                    continue
                for next_word in all_combos[key]:
                    if next_word == endWord:
                        return level + 1
                    if next_word not in visited:
                        visited.add(next_word)
                        q.append((next_word, level + 1))

                all_combos[key] = []

        return 0
