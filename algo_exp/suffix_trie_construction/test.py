from unittest import TestCase, main
from algo_exp.suffix_trie_construction.main import SuffixTrie


trie = SuffixTrie('babc')

class TestSuite(TestCase):
    def test_1(self):
        self.assertDictEqual(trie.root, {
            'c': { '*': True },
            'b': {
                'c': { '*': True },
                'a': { 'b': { 'c': { '*': True } } }
            },
            'a': { 'b': { 'c': { '*': True } } }
        })

    def test_2(self):
        self.assertTrue(trie.contains('abc'))

    def test_3(self):
        self.assertFalse(trie.contains('babcd'))

    def test_4(self):
        self.assertFalse(trie.contains('a'))


if __name__ == '__main__':
    main()
