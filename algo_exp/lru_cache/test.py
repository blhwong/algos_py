from algo_exp.lru_cache.main import LRUCache


def test_1():
    c = LRUCache(3)
    c.insertKeyValuePair('b', 2)
    c.insertKeyValuePair('a', 1)
    c.insertKeyValuePair('c', 3)
    assert c.getMostRecentKey() == 'c'
    assert c.getValueFromKey('a') == 1
    assert c.getMostRecentKey() == 'a'
    c.insertKeyValuePair('d', 4)
    assert c.getValueFromKey('b') == None
    c.insertKeyValuePair('a', 5)
    assert c.getValueFromKey('a') == 5

def test_2():
    c = LRUCache(1)
    assert c.getValueFromKey('a') == None
    c.insertKeyValuePair('a', 1)
    assert c.getValueFromKey('a') == 1
    c.insertKeyValuePair('a', 9001)
    assert c.getValueFromKey('a') == 9001
    c.insertKeyValuePair('b', 2)
    assert c.getValueFromKey('a') == None
    assert c.getValueFromKey('b') == 2
    c.insertKeyValuePair('c', 3)
    assert c.getValueFromKey('a') == None
    assert c.getValueFromKey('b') == None
    assert c.getValueFromKey('c') == 3
