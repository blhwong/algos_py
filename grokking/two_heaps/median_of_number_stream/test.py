from grokking.two_heaps.median_of_number_stream.main import MedianOfAStream


def test_1():
    m = MedianOfAStream()
    m.insert_num(3)
    m.insert_num(1)
    m.insert_num(0)
    result1 = m.find_median()
    m.insert_num(5)
    result2 = m.find_median()
    m.insert_num(4)
    result3 = m.find_median()
    m.insert_num(6)
    result4 = m.find_median()
    m.insert_num(10)
    result5 = m.find_median()
    m.insert_num(10)
    result6 = m.find_median()
    m.insert_num(10)
    result7 = m.find_median()
    m.insert_num(10)
    result8 = m.find_median()
    m.insert_num(10)
    result9 = m.find_median()
    m.insert_num(10)
    result10 = m.find_median()
    m.insert_num(10)
    result11 = m.find_median()

    assert result1 == 1
    assert result2 == 2
    assert result3 == 3
    assert result4 == 3.5
    assert result5 == 4
    assert result6 == 4.5
    assert result7 == 5
    assert result8 == 5.5
    assert result9 == 6
    assert result10 == 8
    assert result11 == 10
