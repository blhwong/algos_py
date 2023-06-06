from leet.unique_morse_representations.main import Solution


s = Solution()


def test_1():
    assert s.uniqueMorseRepresentations(["gin","zen","gig","msg"]) == 2


def test_2():
    assert s.uniqueMorseRepresentations(["a"]) == 1
