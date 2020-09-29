from algo_exp.suffix_trie_construction.main import SuffixTrie


trie = SuffixTrie('babc')


def test_1():
    expected = {
        'c': {'*': True},
        'b': {
            'c': {'*': True},
            'a': {'b': {'c': {'*': True}}}
        },
        'a': {'b': {'c': {'*': True}}}
    }
    assert trie.root == expected


def test_2():
    assert trie.contains('abc') is True


def test_3():
    assert trie.contains('babcd') is False


def test_4():
    assert trie.contains('a') is False
