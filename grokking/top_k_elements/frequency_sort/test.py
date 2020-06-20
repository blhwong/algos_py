from unittest import TestCase, main
from grokking.top_k_elements.frequency_sort.main import sort_character_by_frequency


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(sort_character_by_frequency('Programming'), 'ggmmrrPaino')

    def test_2(self):
        self.assertEqual(sort_character_by_frequency('abcbab'), 'bbbaac')


if __name__ == '__main__':
    main()
