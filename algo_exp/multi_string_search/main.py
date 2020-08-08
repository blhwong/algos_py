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
    found = True
    for char in string:
        if char not in curr:
            found = False
            break
        curr = curr[char]

    return found

def multiStringSearch(bigString, smallStrings):
    bigStrings = bigString.split(' ')
    prefix_trie = Trie(bigStrings)
    suffix_trie = Trie([string[::-1] for string in bigStrings])
    ans = []
    for string in smallStrings:
        ans.append(search_trie(prefix_trie, string) or search_trie(suffix_trie, string[::-1]))

    return ans
