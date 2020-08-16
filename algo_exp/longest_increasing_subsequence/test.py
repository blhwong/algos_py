from algo_exp.longest_increasing_subsequence.main import longestIncreasingSubsequenceBruteForce, longestIncreasingSubsequenceDP, longestIncreasingSubsequence

class TestBruteForce:
    def test_1(self):
        array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
        assert longestIncreasingSubsequenceBruteForce(array) == [-24, 2, 3, 5, 6, 35]

class TestDP:
    def test_1(self):
        array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
        assert longestIncreasingSubsequenceDP(array) == [-24, 2, 3, 5, 6, 35]

    def test_2(self):
        array = [-1]
        assert longestIncreasingSubsequenceDP(array) == [-1]

class TestOptimalSolution:
    def test_1(self):
        array = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
        assert longestIncreasingSubsequence(array) == [-24, 2, 3, 5, 6, 35]
