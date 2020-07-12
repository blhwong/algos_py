# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    def get_removed(descendant):
        curr = descendant
        removed = 0
        while curr != topAncestor:
            curr = curr.ancestor
            removed += 1

        return removed

    def align_descendants(d1_removed, d2_removed):
        d1 = descendantOne
        while d1_removed > d2_removed:
            d1 = d1.ancestor
            d1_removed -= 1

        d2 = descendantTwo
        while d2_removed > d1_removed:
            d2 = d2.ancestor
            d2_removed -= 1

        return d1, d2


    d1_removed = get_removed(descendantOne)
    d2_removed = get_removed(descendantTwo)

    d1, d2 = align_descendants(d1_removed, d2_removed)

    while d1 != d2:
        d1 = d1.ancestor
        d2 = d2.ancestor

    return d1
