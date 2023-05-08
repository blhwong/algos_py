from grokking.top_k_elements.top_k_frequent_numbers.main import find_k_frequent_numbers



def test_1():
    k = 2
    ans = find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], k)
    assert len(ans) == k
    assert 11 in ans
    assert 12 in ans

def test_2():
    k = 2
    ans = find_k_frequent_numbers([5, 12, 11, 3, 11], k)
    assert len(ans) == k
    assert 11 in ans
    assert 3 in ans or 12 in ans or 5 in ans # All of these are valid
