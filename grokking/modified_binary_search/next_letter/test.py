from grokking.modified_binary_search.next_letter.main import search_next_letter


def test_1():
    assert search_next_letter(['a', 'c', 'f', 'h'], 'f') == 'h'

def test_2():
    assert search_next_letter(['a', 'c', 'f', 'h'], 'b') == 'c'

def test_3():
    assert search_next_letter(['a', 'c', 'f', 'h'], 'm') == 'a'

def test_4():
    assert search_next_letter(['a', 'c', 'f', 'h'], 'h') == 'a'
