# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            for j in range(i, len(string)):
                ref = self.root
                for char in string[j:]:
                    if char not in ref:
                        ref[char] = {}
                    ref = ref[char]
                ref['*'] = True

    def contains(self, string):
        ref = self.root
        for char in string:
            if char not in ref:
                return False
            ref = ref[char]

        return ref.get('*') == True
