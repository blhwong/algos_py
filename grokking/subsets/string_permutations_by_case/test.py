from grokking.subsets.string_permutations_by_case.main import find_letter_case_string_permutations


def test_1():
    expected = ['ad52', 'Ad52', 'aD52', 'AD52']
    assert find_letter_case_string_permutations('ad52') == expected

def test_2():
    expected = ['ab7c', 'Ab7c', 'aB7c',
                'AB7c', 'ab7C', 'Ab7C', 'aB7C', 'AB7C']
    assert find_letter_case_string_permutations('ab7c') == expected

def test_3():
    expected = ['AB', 'aB', 'Ab', 'ab']
    assert find_letter_case_string_permutations('AB') == expected
