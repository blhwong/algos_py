from grokking.top_k_elements.rearrange_string.main import rearrange_string


def test_1():
    assert rearrange_string('aappp') == 'papap'

def test_2():
    assert rearrange_string('Programming') == 'gmrPagimnor'


def test_3():
    assert rearrange_string('aapa') == ''

