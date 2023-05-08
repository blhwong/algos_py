from grokking.top_k_elements.frequency_sort.main import sort_character_by_frequency


def test_1():
    assert sort_character_by_frequency('Programming') == 'ggmmrrPaino'

def test_2():
    assert sort_character_by_frequency('abcbab') == 'bbbaac'
