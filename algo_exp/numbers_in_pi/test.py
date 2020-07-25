from unittest import TestCase, main
from algo_exp.numbers_in_pi.main import numbersInPi

pi = '3141592653589793238462643383279'

class TestSuite(TestCase):
    def test_1(self):
        numbers = [
            '314159265358979323846',
            '26433',
            '8',
            '3279',
            '314159265',
            '35897932384626433832',
            '79',
        ]
        self.assertEqual(numbersInPi(pi, numbers), 2)


    def test_2(self):
        numbers = [
            '141592653589793238462643383279',
            '314159265358979323846',
            '327',
            '26433',
            '8',
            '3279',
            '9',
            '314159265',
            '35897932384626433832',
            '79',
            '3'
        ]
        self.assertEqual(numbersInPi(pi, numbers), 1)

    def test_3(self):
        numbers = [
            '3',
            '314',
            '49',
            '9001',
            '15926535897',
            '14',
            '9323',
            '8462643383279',
            '4',
            '793',
        ]
        self.assertEqual(numbersInPi(pi, numbers), 3)

if __name__ == '__main__':
    main()
