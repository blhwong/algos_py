from grokking_dp.longest_common_substring.subsequence_pattern_matching.main import find_spm_count


def test_1():
    assert find_spm_count("baxmx", "ax") == 2


def test_2():
    assert find_spm_count("tomorrow", "tor") == 4
