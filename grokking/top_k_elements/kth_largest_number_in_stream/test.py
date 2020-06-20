from unittest import TestCase, main
from grokking.top_k_elements.kth_largest_number_in_stream.main import KthLargestNumberInStream


class TestSuite(TestCase):
    def test_1(self):
        stream = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
        result1 = stream.add(6)
        result2 = stream.add(13)
        result3 = stream.add(6)

        self.assertEqual(result1, 5)
        self.assertEqual(result2, 6)
        self.assertEqual(result3, 6)

    def test_2(self):
        stream = KthLargestNumberInStream([1, 5, 10, 2], 1)
        result1 = stream.add(1)
        result2 = stream.add(11)
        result3 = stream.add(2)

        self.assertEqual(result1, 10)
        self.assertEqual(result2, 11)
        self.assertEqual(result3, 11)

    def test_3(self):
        stream = KthLargestNumberInStream([1, 5, 10, 2], 4)
        result1 = stream.add(1)
        result2 = stream.add(11)
        result3 = stream.add(9)

        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 5)

if __name__ == '__main__':
    main()
