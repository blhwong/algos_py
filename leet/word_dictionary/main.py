class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_symbol = '*'


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        curr = self.root
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]

        curr[self.end_symbol] = True

    def search_from_trie(self, word, trie):
        curr = trie
        for i, char in enumerate(word):
            char = word[i]
            if char == '.':
                for key, t in curr.items():
                    if key == self.end_symbol:
                        continue
                    found = self.search_from_trie(word[i + 1:], t)
                    if found:
                        return True

                return False
            if char not in curr:
                return False
            curr = curr[char]

        return self.end_symbol in curr


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        return self.search_from_trie(word, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
