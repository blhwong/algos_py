from unittest import TestCase, main
from algo_exp.lru_cache.main import LRUCache


class TestSuite(TestCase):
    def test_1(self):
        c = LRUCache(3)
        c.insertKeyValuePair('b', 2)
        c.insertKeyValuePair('a', 1)
        c.insertKeyValuePair('c', 3)
        self.assertEqual(c.getMostRecentKey(), 'c')
        self.assertEqual(c.getValueFromKey('a'), 1)
        self.assertEqual(c.getMostRecentKey(), 'a')
        c.insertKeyValuePair('d', 4)
        self.assertEqual(c.getValueFromKey('b'), None)
        c.insertKeyValuePair('a', 5)
        self.assertEqual(c.getValueFromKey('a'), 5)

    def test_2(self):
        c = LRUCache(1)
        self.assertEqual(c.getValueFromKey('a'), None)
        c.insertKeyValuePair('a', 1)
        self.assertEqual(c.getValueFromKey('a'), 1)
        c.insertKeyValuePair('a', 9001)
        self.assertEqual(c.getValueFromKey('a'), 9001)
        c.insertKeyValuePair('b', 2)
        self.assertEqual(c.getValueFromKey('a'), None)
        self.assertEqual(c.getValueFromKey('b'), 2)
        c.insertKeyValuePair('c', 3)
        self.assertEqual(c.getValueFromKey('a'), None)
        self.assertEqual(c.getValueFromKey('b'), None)
        self.assertEqual(c.getValueFromKey('c'), 3)


if __name__ == '__main__':
    main()
