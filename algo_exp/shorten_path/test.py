from unittest import TestCase, main
from algo_exp.shorten_path.main import shortenPath


class TestSuite(TestCase):
    def test_1(self):
        self.assertEqual(shortenPath('/foo/../test/../test/../foo//bar/./baz'), '/foo/bar/baz')

    def test_2(self):
        self.assertEqual(shortenPath('/../../foo/../../bar/baz'), '/bar/baz')

    def test_3(self):
        self.assertEqual(shortenPath('../../foo/bar/baz'), '../../foo/bar/baz')

    def test_3(self):
        self.assertEqual(shortenPath('../../foo/../../bar/baz'), '../../../bar/baz')

    def test_4(self):
        self.assertEqual(shortenPath('foo/../..'), '..')

    def test_5(self):
        self.assertEqual(shortenPath('/'), '/')

if __name__ == '__main__':
    main()
