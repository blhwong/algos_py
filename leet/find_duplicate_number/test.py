from leet.find_duplicate_number.main import Solution


s = Solution()


def test_1():
    assert s.findDuplicate([1, 3, 4, 2, 2]) == 2
    assert s.findDuplicateCyclic([1, 3, 4, 2, 2]) == 2


def test_2():
    assert s.findDuplicate([3, 1, 3, 4, 2]) == 3
    assert s.findDuplicateCyclic([3, 1, 3, 4, 2]) == 3


def test_3():
    assert s.findDuplicate([1, 1]) == 1
    assert s.findDuplicateCyclic([1, 1]) == 1


def test_4():
    assert s.findDuplicate([1, 1, 2]) == 1
    assert s.findDuplicateCyclic([1, 1, 2]) == 1
