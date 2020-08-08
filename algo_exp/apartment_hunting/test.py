from unittest import TestCase, main
from algo_exp.apartment_hunting.main import apartmentHunting


class TestSuite(TestCase):
    def test_1(self):
        result = apartmentHunting([
            { 'gym': False, 'school': True, 'store': False },
            { 'gym': True, 'school': False, 'store': False },
            { 'gym': True, 'school': True, 'store': False },
            { 'gym': False, 'school': True, 'store': False },
            { 'gym': False, 'school': True, 'store': True },
        ], ['gym', 'school', 'store'])
        self.assertEqual(result, 3)


if __name__ == '__main__':
    main()
