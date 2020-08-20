from leet.word_dictionary.main import WordDictionary


def test_1():
    wd = WordDictionary()
    wd.addWord('bad')
    wd.addWord('dad')
    wd.addWord('mad')
    assert wd.search('pad') is False
    assert wd.search('bad') is True
    assert wd.search('.ad') is True
    assert wd.search('b..') is True



def test_2():
    wd = WordDictionary()
    wd.addWord('a')
    assert wd.search('.') is True
    assert wd.search('.a') is False
    assert wd.search('a.') is False
