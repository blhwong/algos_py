from unittest import TestCase, main
from algo_exp.multi_string_search.main import multiStringSearch


class TestSuite(TestCase):
    def test_1(self):
        result = multiStringSearch('this is a big string', ['this', 'yo', 'is', 'a', 'bigger', 'string', 'kappa'])
        expected = [True, False, True, True, False, True, False]
        self.assertListEqual(result, expected)

    def test_2(self):
        result = multiStringSearch('Mary goes to the shopping center every week', ['to', 'Mary', 'centers', 'shop', 'shopping', 'string', 'kappa'])
        expected = [True, True, False, True, True, False, False]
        self.assertListEqual(result, expected)

    def test_3(self):
        result = multiStringSearch("this ain't a big string", ['this', 'is', 'yo', 'a', 'bigger'])
        expected = [True, True, False, True, False]
        self.assertListEqual(result, expected)

    def test_4(self):
        result = multiStringSearch('adcb akfkw afnmc fkadn vkaca jdaf jacb cdba cbda', ['abcd', 'acbd', 'adbc', 'dabc', 'cbda', 'cabd', 'cdab'])
        expected = [False, False, False, False, True, False, False]
        self.assertListEqual(result, expected)


if __name__ == '__main__':
    main()
