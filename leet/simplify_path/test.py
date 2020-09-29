from leet.simplify_path.main import Solution


s = Solution()


def test_1():
    assert s.simplifyPath('/home/') == '/home'


def test_2():
    assert s.simplifyPath('/../') == '/'


def test_3():
    assert s.simplifyPath('/home//foo/') == '/home/foo'


def test_4():
    assert s.simplifyPath('/a/./b/../../c/') == '/c'


def test_5():
    assert s.simplifyPath('/a/../../b/../c//.//') == '/c'


def test_6():
    assert s.simplifyPath('/a//b////c/d//././/..') == '/a/b/c'
