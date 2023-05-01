from data_structures.interval import Interval


def test_compare_same():
    intervals1 = []
    intervals2 = []

    intervals1.append(Interval(1, 2))
    intervals1.append(Interval(3, 4))
    intervals1.append(Interval(10, 15))

    intervals2.append(Interval(1, 2))
    intervals2.append(Interval(3, 4))
    intervals2.append(Interval(10, 15))

    assert intervals1 == intervals2


def test_compare_different_length():
    intervals1 = []
    intervals2 = []

    intervals1.append(Interval(1, 2))
    intervals1.append(Interval(3, 4))
    intervals1.append(Interval(10, 15))

    intervals2.append(Interval(1, 2))
    intervals2.append(Interval(3, 4))

    assert intervals1 != intervals2


def test_compare_different_values():
    intervals1 = []
    intervals2 = []

    intervals1.append(Interval(1, 2))
    intervals1.append(Interval(3, 4))
    intervals1.append(Interval(10, 15))

    intervals2.append(Interval(2, 4))
    intervals2.append(Interval(3, 6))
    intervals2.append(Interval(10, 15))

    assert intervals1 != intervals2
