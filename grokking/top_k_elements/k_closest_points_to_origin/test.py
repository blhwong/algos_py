from unittest import TestCase, main
from grokking.top_k_elements.k_closest_points_to_origin.main import find_closest_points, Point


class TestSuite(TestCase):
    def test_1(self):
        result = find_closest_points([Point(1, 2), Point(1, 3)], 1)
        expected = [Point(1, 2)]
        self.assertTrue(Point.compare(result, expected))

    def test_2(self):
        result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
        expected = [Point(1, 3), Point(2, -1)]
        self.assertTrue(Point.compare(result, expected))


if __name__ == '__main__':
    main()
