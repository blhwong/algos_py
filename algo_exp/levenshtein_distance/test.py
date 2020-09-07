from algo_exp.levenshtein_distance.main import levenshtein_distance


def test_1():
    assert levenshtein_distance('abc', 'yabd') == 2
