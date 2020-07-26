from unittest import TestCase, main
from misc.calculator.main import calculate


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(calculate('5+16-((9-6)-(4-2))+1'), 21)

    def test_2(self):
        self.assertEqual(calculate('22+(2-4)'), 20)

    def test_3(self):
        self.assertEqual(calculate('6+9-12'), 3)

    def test_4(self):
        self.assertEqual(calculate('((1024))'), 1024)

    def test_5(self):
        self.assertEqual(calculate('255'), 255)

    def test_6(self):
        self.assertEqual(calculate('5+2-1+10-3+1'), 14)

    def test_7(self):
        self.assertEqual(calculate('-1-2-3'), -6)

    def test_8(self):
        self.assertEqual(calculate('1 + 1'), 2)

    def test_9(self):
        self.assertEqual(calculate(' 2-1 + 2 '), 3)

    def test_10(self):
        self.assertEqual(calculate('(1+(4+5+2)-3)+(6+8)'), 23)

    def test_11(self):
        self.assertEqual(calculate('2-(5-6)'), 3)

    def test_12(self):
        self.assertEqual(calculate('(5-(1+(5)))'), -1)


if __name__ == '__main__':
    main()
