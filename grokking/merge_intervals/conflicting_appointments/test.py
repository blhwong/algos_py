from grokking.merge_intervals.conflicting_appointments.main import can_attend_all_appointments


def test_1():
    assert not can_attend_all_appointments([[1, 4], [2, 5], [7, 9]])

def test_2():
    assert can_attend_all_appointments([[6, 7], [2, 4], [8, 12]])

def test_3():
    assert not can_attend_all_appointments([[4, 5], [2, 3], [3, 6]])

def test_4():
    assert can_attend_all_appointments([[1, 3], [3, 5], [5, 10]])
