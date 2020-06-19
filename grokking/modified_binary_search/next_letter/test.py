from unittest import TestCase, main
from grokking.modified_binary_search.next_letter.main import search_next_letter


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(search_next_letter(['a', 'c', 'f', 'h'], 'f'), 'h')

    def test_2(self):
        self.assertEqual(search_next_letter(['a', 'c', 'f', 'h'], 'b'), 'c')

    def test_3(self):
        self.assertEqual(search_next_letter(['a', 'c', 'f', 'h'], 'm'), 'a')

    def test_4(self):
        self.assertEqual(search_next_letter(['a', 'c', 'f', 'h'], 'h'), 'a')

if __name__ == '__main__':
    main()
