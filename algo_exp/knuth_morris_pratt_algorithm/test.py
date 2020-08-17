from algo_exp.knuth_morris_pratt_algorithm.main import knuthMorrisPrattAlgorithm


def test_1():
    assert knuthMorrisPrattAlgorithm('aefoaefcdaefcdaed', 'aefcdaed') is True

def test_2():
    assert knuthMorrisPrattAlgorithm('aefaefaefaedaefaedaefaefa', 'aefaedaefaefa') is True
