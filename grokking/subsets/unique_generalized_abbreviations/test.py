from unittest import TestCase, main
from grokking.subsets.unique_generalized_abbreviations.main import generate_generalized_abbreviation, generate_generalized_abbreviation_recursive


class TestSuite(TestCase):
    def test_1(self):
        expected = ["BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"]
        self.assertCountEqual(generate_generalized_abbreviation('BAT'), expected)

    def test_2(self):
        expected = ["code", "cod1", "co1e", "co2", "c1de", "c1d1", "c2e", "c3", "1ode", "1od1", "1o1e", "1o2",
                    "2de", "2d1", "3e", "4"]
        self.assertCountEqual(generate_generalized_abbreviation('code'), expected)

    def test_3(self):
        expected = ["BAT", "BA1", "B1T", "B2", "1AT", "1A1", "2T", "3"]
        self.assertCountEqual(generate_generalized_abbreviation_recursive('BAT'), expected)

    def test_4(self):
        expected = ["code", "cod1", "co1e", "co2", "c1de", "c1d1", "c2e", "c3", "1ode", "1od1", "1o1e", "1o2",
                    "2de", "2d1", "3e", "4"]
        self.assertCountEqual(generate_generalized_abbreviation_recursive('code'), expected)


if __name__ == '__main__':
    main()
