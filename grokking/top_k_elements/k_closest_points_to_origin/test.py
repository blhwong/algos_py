from grokking.top_k_elements.k_closest_points_to_origin.main import find_closest_points, Point


def test_1():
    result = find_closest_points([Point(1, 2), Point(1, 3)], 1)
    expected = [Point(1, 2)]
    assert Point.compare(result, expected)

def test_2():
    result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
    expected = [Point(1, 3), Point(2, -1)]
    assert Point.compare(result, expected)
