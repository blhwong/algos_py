from unittest import TestCase, main
from grokking.merge_intervals.conflicting_appointments.main import can_attend_all_appointments


class TestSuite(TestCase):
    def test_1(self):
        self.assertFalse(can_attend_all_appointments([[1, 4], [2, 5], [7, 9]]))


    def test_2(self):
        self.assertTrue(can_attend_all_appointments([[6, 7], [2, 4], [8, 12]]))


    def test_3(self):
        self.assertFalse(can_attend_all_appointments([[4, 5], [2, 3], [3, 6]]))


if __name__ == '__main__':
    main()
