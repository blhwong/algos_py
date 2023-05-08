from grokking.top_k_elements.kth_largest_number_in_stream.main import KthLargestNumberInStream


def test_1():
    stream = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
    result1 = stream.add(6)
    result2 = stream.add(13)
    result3 = stream.add(6)

    assert result1 == 5
    assert result2 == 6
    assert result3 == 6

def test_2():
    stream = KthLargestNumberInStream([1, 5, 10, 2], 1)
    result1 = stream.add(1)
    result2 = stream.add(11)
    result3 = stream.add(2)

    assert result1 == 10
    assert result2 == 11
    assert result3 == 11

def test_3():
    stream = KthLargestNumberInStream([1, 5, 10, 2], 4)
    result1 = stream.add(1)
    result2 = stream.add(11)
    result3 = stream.add(9)

    assert result1 == 1
    assert result2 == 2
    assert result3 == 5
