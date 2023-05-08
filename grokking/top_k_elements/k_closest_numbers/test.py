from unittest import TestCase, main
from grokking.top_k_elements.k_closest_numbers.main import find_closest_elements, find_closest_elements_bs, find_closest_elements_tp


class TestSuite(TestCase):
    def test_1(self):
        self.assertCountEqual(find_closest_elements([5, 6, 7, 8, 9], 3, 7), [6, 7, 8])

    def test_2(self):
        self.assertCountEqual(find_closest_elements([2, 4, 5, 6, 9], 3, 6), [4, 5, 6])

    def test_3(self):
        self.assertCountEqual(find_closest_elements([2, 4, 5, 6, 9], 3, 10), [5, 6, 9])

    def test_4(self):
        self.assertCountEqual(find_closest_elements_bs([5, 6, 7, 8, 9], 3, 7), [6, 7, 8])

    def test_5(self):
        self.assertCountEqual(find_closest_elements_bs([2, 4, 5, 6, 9], 3, 6), [4, 5, 6])

    def test_6(self):
        self.assertCountEqual(find_closest_elements_bs([2, 4, 5, 6, 9], 3, 10), [5, 6, 9])

    def test_7(self):
        self.assertCountEqual(find_closest_elements_tp([5, 6, 7, 8, 9], 3, 7), [6, 7, 8])

    def test_8(self):
        self.assertCountEqual(find_closest_elements_tp([2, 4, 5, 6, 9], 3, 6), [4, 5, 6])

    def test_9(self):
        self.assertCountEqual(find_closest_elements_tp([2, 4, 5, 6, 9], 3, 10), [5, 6, 9])

    def test_10(self):
        self.assertCountEqual(find_closest_elements_tp([2, 4, 5, 6, 9], 3, 2), [2, 4, 5])

    def test_11(self):
        self.assertCountEqual(find_closest_elements_tp([2, 4, 5, 6, 9], 3, 4), [2, 4, 5])

    def test_12(self):
        self.assertCountEqual(find_closest_elements_tp([2, 4, 5, 6, 9], 3, 6), [4, 5, 6])

if __name__ == '__main__':
    main()
