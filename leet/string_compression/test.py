from leet.string_compression.main import Solution


s = Solution()


def test_1():
    chars = ["a", "a", "b", "b", "c", "c", "c"]
    expected = ["a", "2", "b", "2", "c", "3"]
    res = s.compress(chars)
    assert chars[:res] == expected


def test_2():
    chars = ["a"]
    expected = ["a"]
    res = s.compress(chars)
    assert chars[:res] == expected


def test_3():
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    expected = ["a", "b", "1", "2"]
    res = s.compress(chars)
    assert chars[:res] == expected
