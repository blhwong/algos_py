from unittest import TestCase, main
from grokking.modified_binary_search.ceiling_of_a_number.main import search_ceiling_of_a_number, search_floor_of_a_number


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(search_ceiling_of_a_number([4, 6, 10], 6), 1)

    def test_2(self):
        self.assertEqual(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12), 4)

    def test_3(self):
        self.assertEqual(search_ceiling_of_a_number([4, 6, 10], 17), -1)

    def test_4(self):
        self.assertEqual(search_ceiling_of_a_number([4, 6, 10], -1), 0)

    def test_5(self):
        self.assertEqual(search_floor_of_a_number([4, 6, 10], 6), 1)

    def test_6(self):
        self.assertEqual(search_floor_of_a_number([1, 3, 8, 10, 15], 12), 3)

    def test_7(self):
        self.assertEqual(search_floor_of_a_number([4, 6, 10], 17), 2)

    def test_8(self):
        self.assertEqual(search_floor_of_a_number([4, 6, 10], -1), -1)

if __name__ == '__main__':
    main()
