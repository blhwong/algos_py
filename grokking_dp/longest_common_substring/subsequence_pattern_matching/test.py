from grokking_dp.longest_common_substring.subsequence_pattern_matching.main import find_spm_count_recursive, find_spm_count_iterative


def test_1():
    assert find_spm_count_recursive("baxmx", "ax") == 2


def test_2():
    assert find_spm_count_recursive("tomorrow", "tor") == 4


def test_3():
    assert find_spm_count_iterative("baxmx", "ax") == 2


def test_4():
    assert find_spm_count_iterative("tomorrow", "tor") == 4
