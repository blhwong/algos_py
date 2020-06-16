from unittest import TestCase, main
from grokking.two_heaps.sliding_window_median.main import SlidingWindowMedian

s = SlidingWindowMedian()

class TestSuite(TestCase):
    def test_1(self):
        result = s.find_sliding_window_median([1, 2, -1, 3, 5], 2)
        expected = [1.5, 0.5, 1.0, 4.0]
        self.assertListEqual(result, expected)

    def test_2(self):
        result = s.find_sliding_window_median([1, 2, -1, 3, 5], 3)
        expected = [1.0, 2.0, 3.0]
        self.assertListEqual(result, expected)

if __name__ == '__main__':
    main()
