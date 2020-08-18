class Trie:
    def __init__(self, strings):
        self.end_symbol = '*'
        self.root = self.build_trie(strings)

    def build_trie(self, strings):
        root = {}
        for string in strings:
            curr = root
            for char in string:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr[self.end_symbol] = True
        return root

def search_trie(t, string):
    curr = t.root

    for char in string:
        if char not in curr:
            return False
        curr = curr[char]

    return True

def multiStringSearch(bigString, smallStrings):
    big_strings = bigString.split(' ')
    prefix_trie = Trie(big_strings)
    suffix_trie = Trie([string[::-1] for string in big_strings])

    ans = []
    for string in smallStrings:
        ans.append(search_trie(prefix_trie, string) or search_trie(suffix_trie, string[::-1]))

    return ans
