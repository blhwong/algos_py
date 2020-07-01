from unittest import TestCase, main
from leet.contains_duplicate.main import Solution


s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(s.containsDuplicate([1, 2, 3, 1]))

    def test_2(self):
        self.assertFalse(s.containsDuplicate([1, 2, 3, 4]))

    def test_3(self):
        self.assertTrue(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

if __name__ == '__main__':
    main()
