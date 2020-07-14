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



if __name__ == '__main__':
    main()
