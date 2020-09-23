from leet.employee_free_time.main import Solution, Interval


s = Solution()


def test_1():
    result = s.employeeFreeTime([
        [
            Interval(1, 2),
            Interval(5, 6),
        ],
        [
            Interval(1, 3),
        ],
        [
            Interval(4, 10),
        ],
    ])
    assert result == [Interval(3, 4)]


def test_2():
    result = s.employeeFreeTime([
        [
            Interval(1, 3),
            Interval(6, 7),
        ],
        [
            Interval(2, 4),
            Interval(2, 5),
            Interval(9, 12),
        ],
    ])
    assert result == [Interval(5, 6), Interval(7, 9)]


def test_3():
    """
    [6, 24], [29, 33], [43, 59], [61, 75], [80, 81], [94, 99]
    """
    result = s.employeeFreeTime([
        [
            Interval(7, 24),
            Interval(29, 33),
            Interval(45, 57),
            Interval(66, 69),
            Interval(94, 99),
        ],
        [
            Interval(6, 24),
            Interval(43, 49),
            Interval(56, 59),
            Interval(61, 75),
            Interval(80, 81),
        ],
        [
            Interval(5, 16),
            Interval(18, 26),
            Interval(33, 36),
            Interval(39, 57),
            Interval(65, 74),
        ],
        [
            Interval(9, 16),
            Interval(27, 35),
            Interval(40, 55),
            Interval(68, 71),
            Interval(78, 81),
        ],
        [
            Interval(0, 25),
            Interval(29, 31),
            Interval(40, 47),
            Interval(57, 87),
            Interval(91, 94),
        ],
    ])

    assert result == [
        Interval(26, 27),
        Interval(36, 39),
        Interval(87, 91),
    ]
