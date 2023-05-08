from grokking.bitwise_xor.complement_of_base_10.main import calculate_bitwise_complement


def test_1():
    assert calculate_bitwise_complement(8) == 7

def test_2():
    assert calculate_bitwise_complement(10) == 5
