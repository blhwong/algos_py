from leet.remove_duplicates_from_sorted_array.main import Solution

s = Solution()

def test_1():
    nums = [1, 1, 2, 2, 3, 3]
    k = s.removeDuplicates(nums)
    assertion_helper(nums, [1, 2, 3], k)

def test_2():
    nums = [1, 1, 2]
    k = s.removeDuplicates(nums)
    assertion_helper(nums, [1, 2], k)

def test_3():
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k = s.removeDuplicates(nums)
    assertion_helper(nums, [0, 1, 2, 3, 4], k)

def test_4():
    nums = [1, 2]
    k = s.removeDuplicates(nums)
    assertion_helper(nums, [1, 2], k)

def test_5():
    nums = [1]
    k = s.removeDuplicates(nums)
    assertion_helper(nums, [1], k)

def test_6():
    nums = [1, 2, 3]
    k = s.removeDuplicates(nums)
    assertion_helper(nums, [1, 2, 3], k)

def assertion_helper(nums, expected_nums, k):
    print(nums, expected_nums, k)
    assert len(expected_nums) == k
    for i in range(k):
        assert nums[i] == expected_nums[i]
