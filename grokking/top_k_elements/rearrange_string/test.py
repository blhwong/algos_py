from unittest import TestCase, main
from grokking.top_k_elements.rearrange_string.main import rearrange_string


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(rearrange_string('aappp'), 'papap')

    def test_2(self):
        self.assertEqual(rearrange_string('Programming'), 'gmrPagimnor')


    def test_3(self):
        self.assertEqual(rearrange_string('aapa'), '')


if __name__ == '__main__':
    main()
