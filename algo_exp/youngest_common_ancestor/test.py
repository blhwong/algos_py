from unittest import TestCase, main
from algo_exp.youngest_common_ancestor.main import AncestralTree, getYoungestCommonAncestor


class TestSuite(TestCase):
    def test_1(self):
        a = AncestralTree('A')
        b = AncestralTree('B')
        b.ancestor = a
        c = AncestralTree('C')
        c.ancestor = a
        d = AncestralTree('D')
        d.ancestor = b
        e = AncestralTree('E')
        e.ancestor = b
        h = AncestralTree('H')
        h.ancestor = d
        i = AncestralTree('I')
        i.ancestor = d
        f = AncestralTree('F')
        f.ancestor = c
        g = AncestralTree('G')
        g.ancestor = c
        self.assertEqual(getYoungestCommonAncestor(a, e, i), b)


if __name__ == '__main__':
    main()
