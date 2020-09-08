from algo_exp.youngest_common_ancestor.main import AncestralTree, get_youngest_common_ancestor


def test_1():
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
    assert get_youngest_common_ancestor(a, e, i) == b
