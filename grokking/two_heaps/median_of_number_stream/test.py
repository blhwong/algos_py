from unittest import TestCase, main
from grokking.two_heaps.median_of_number_stream.main import MedianOfAStream


class TestSuite(TestCase):
    def test_1(self):
        m = MedianOfAStream()
        m.insert_num(3)
        m.insert_num(1)
        m.insert_num(0)
        result1 = m.find_median()
        m.insert_num(5)
        result2 = m.find_median()
        m.insert_num(4)
        result3 = m.find_median()
        m.insert_num(6)
        result4 = m.find_median()
        m.insert_num(10)
        result5 = m.find_median()
        m.insert_num(10)
        result6 = m.find_median()
        m.insert_num(10)
        result7 = m.find_median()
        m.insert_num(10)
        result8 = m.find_median()
        m.insert_num(10)
        result9 = m.find_median()
        m.insert_num(10)
        result10 = m.find_median()
        m.insert_num(10)
        result11 = m.find_median()

        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)
        self.assertEqual(result3, 3)
        self.assertEqual(result4, 3.5)
        self.assertEqual(result5, 4)
        self.assertEqual(result6, 4.5)
        self.assertEqual(result7, 5)
        self.assertEqual(result8, 5.5)
        self.assertEqual(result9, 6)
        self.assertEqual(result10, 8)
        self.assertEqual(result11, 10)


if __name__ == '__main__':
    main()
