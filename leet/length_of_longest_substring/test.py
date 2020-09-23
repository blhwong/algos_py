from leet.length_of_longest_substring.main import Solution


s = Solution()


def test_1():
    assert s.lengthOfLongestSubstring('abcabcbb') == 3

def test_2():
    assert s.lengthOfLongestSubstring('bbbbb') == 1

def test_3():
    assert s.lengthOfLongestSubstring('pwwkew') == 3

def test_4():
    assert s.lengthOfLongestSubstring('') == 0

def test_5():
    assert s.lengthOfLongestSubstring('dvdf') == 3

def test_5():
    assert s.lengthOfLongestSubstring('anviaj') == 5

def test_6():
    assert s.lengthOfLongestSubstring('abba') == 2
