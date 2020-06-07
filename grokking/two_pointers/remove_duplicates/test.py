from unittest import TestCase, main
from grokking.two_pointers.remove_duplicates.main import remove_duplicates


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(remove_duplicates([2, 3, 3, 3, 6, 9, 9]), 4)

    def test_2(self):
        self.assertEqual(remove_duplicates([2, 2, 2, 11]), 2)


if __name__ == '__main__':
    main()
