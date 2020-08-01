from unittest import TestCase, main
from algo_exp.interweaving_strings.main import interweavingStrings


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(interweavingStrings('algoexpert', 'your-dream-job', 'your-algodream-expertjob'))

    def test_2(self):
        self.assertFalse(interweavingStrings('a', 'b', 'ac'))

    def test_3(self):
        self.assertFalse(interweavingStrings('algoexpert', 'your-dream-job', 'your-algodream-expertjo'))

if __name__ == '__main__':
    main()
