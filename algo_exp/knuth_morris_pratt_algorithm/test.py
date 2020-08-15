from unittest import TestCase, main
from algo_exp.knuth_morris_pratt_algorithm.main import knuthMorrisPrattAlgorithm


class TestSuite(TestCase):
    def test_1(self):
        self.assertTrue(knuthMorrisPrattAlgorithm('aefoaefcdaefcdaed', 'aefcdaed'))

    def test_2(self):
        self.assertTrue(knuthMorrisPrattAlgorithm('aefaefaefaedaefaedaefaefa', 'aefaedaefaefa'))


if __name__ == '__main__':
    main()
