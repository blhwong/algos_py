from unittest import TestCase, main
from grokking.subsets.string_permutations_by_case.main import find_letter_case_string_permutations


class TestSuite(TestCase):
    def test_1(self):
        expected = ["ad52", "Ad52", "aD52", "AD52"]
        self.assertListEqual(find_letter_case_string_permutations('ad52'), expected)

    def test_2(self):
        expected = ["ab7c", "Ab7c", "aB7c",
                    "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]
        self.assertListEqual(find_letter_case_string_permutations('ab7c'), expected)


if __name__ == '__main__':
    main()
