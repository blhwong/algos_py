from unittest import TestCase, main
from algo_exp.continuous_median.main import ContinuousMedianHandler


class TestSuite(TestCase):
    def test_1(self):
        m = ContinuousMedianHandler()
        m.insert(3)
        m.insert(1)
        m.insert(0)
        result1 = m.getMedian()
        m.insert(5)
        result2 = m.getMedian()
        m.insert(4)
        result3 = m.getMedian()
        m.insert(6)
        result4 = m.getMedian()
        m.insert(10)
        result5 = m.getMedian()
        m.insert(10)
        result6 = m.getMedian()
        m.insert(10)
        result7 = m.getMedian()
        m.insert(10)
        result8 = m.getMedian()
        m.insert(10)
        result9 = m.getMedian()
        m.insert(10)
        result10 = m.getMedian()
        m.insert(10)
        result11 = m.getMedian()

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
