from algo_exp.lru_cache.main import LRUCache


def test_1():
    c = LRUCache(3)
    c.insert_key_value_pair('b', 2)
    c.insert_key_value_pair('a', 1)
    c.insert_key_value_pair('c', 3)
    assert c.get_most_recent_key() == 'c'
    assert c.get_value_from_key('a') == 1
    assert c.get_most_recent_key() == 'a'
    c.insert_key_value_pair('d', 4)
    assert c.get_value_from_key('b') == None
    c.insert_key_value_pair('a', 5)
    assert c.get_value_from_key('a') == 5

def test_2():
    c = LRUCache(1)
    assert c.get_value_from_key('a') == None
    c.insert_key_value_pair('a', 1)
    assert c.get_value_from_key('a') == 1
    c.insert_key_value_pair('a', 9001)
    assert c.get_value_from_key('a') == 9001
    c.insert_key_value_pair('b', 2)
    assert c.get_value_from_key('a') == None
    assert c.get_value_from_key('b') == 2
    c.insert_key_value_pair('c', 3)
    assert c.get_value_from_key('a') == None
    assert c.get_value_from_key('b') == None
    assert c.get_value_from_key('c') == 3
