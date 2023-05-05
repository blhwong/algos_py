from grokking.modified_binary_search.search_sorted_infinite_array.main import search_in_infinite_array, ArrayReader

reader1 = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
reader2 = ArrayReader([1, 3, 8, 10, 15])

def test_1():
    assert search_in_infinite_array(reader1, 16) == 6

def test_2():
    assert search_in_infinite_array(reader1, 11) == -1

def test_3():
    assert search_in_infinite_array(reader2, 15) == 4

def test_4():
    assert search_in_infinite_array(reader2, 200) == -1
