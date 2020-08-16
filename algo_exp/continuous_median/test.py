from algo_exp.continuous_median.main import ContinuousMedianHandler


def test_1():
    m = ContinuousMedianHandler()
    m.insert(3)
    m.insert(1)
    m.insert(0)
    result1 = m.getMedian()
    m.insert(5)
    result2 = m.getMedian()
    m.insert(4)
    result3 = m.getMedian()
    m.insert(6)
    result4 = m.getMedian()
    m.insert(10)
    result5 = m.getMedian()
    m.insert(10)
    result6 = m.getMedian()
    m.insert(10)
    result7 = m.getMedian()
    m.insert(10)
    result8 = m.getMedian()
    m.insert(10)
    result9 = m.getMedian()
    m.insert(10)
    result10 = m.getMedian()
    m.insert(10)
    result11 = m.getMedian()

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
