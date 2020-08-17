from algo_exp.levenshtein_distance.main import levenshteinDistance


def test_1():
    assert levenshteinDistance('abc', 'yabd') == 2
