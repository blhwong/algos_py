from grokking.sliding_window.length_of_longest_substring.main import length_of_longest_substring


def test_1():
    length_of_longest_substring('aabccbb', 2) == 5

def test_2():
    length_of_longest_substring('abbcb', 1) == 4

def test_3():
    length_of_longest_substring('abccde', 1) == 3

def test_4():
    length_of_longest_substring('abbcb', 2) == 5
