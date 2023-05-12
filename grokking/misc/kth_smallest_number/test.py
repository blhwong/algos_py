from grokking.misc.kth_smallest_number.main import *


def test_brute_force_1():
    assert find_Kth_smallest_number_brute_force([1, 5, 12, 2, 11, 5], 3) == 5

def test_brute_force_2():
    assert find_Kth_smallest_number_brute_force([1, 5, 12, 2, 11, 5], 4) == 5

def test_brute_force_3():
    assert find_Kth_smallest_number_brute_force([5, 12, 11, -1, 12], 3) == 11

def test_brute_force_sorting_1():
    assert find_Kth_smallest_number_brute_force_sorting([1, 5, 12, 2, 11, 5], 3) == 5

def test_brute_force_sorting_2():
    assert find_Kth_smallest_number_brute_force_sorting([1, 5, 12, 2, 11, 5], 4) == 5

def test_brute_force_sorting_3():
    assert find_Kth_smallest_number_brute_force_sorting([5, 12, 11, -1, 12], 3) == 11

def test_max_heap_1():
    assert find_Kth_smallest_number_max_heap([1, 5, 12, 2, 11, 5], 3) == 5

def test_max_heap_2():
    assert find_Kth_smallest_number_max_heap([1, 5, 12, 2, 11, 5], 4) == 5

def test_max_heap_3():
    assert find_Kth_smallest_number_max_heap([5, 12, 11, -1, 12], 3) == 11

def test_min_heap_1():
    assert find_Kth_smallest_number_min_heap([1, 5, 12, 2, 11, 5], 3) == 5

def test_min_heap_2():
    assert find_Kth_smallest_number_min_heap([1, 5, 12, 2, 11, 5], 4) == 5

def test_min_heap_3():
    assert find_Kth_smallest_number_min_heap([5, 12, 11, -1, 12], 3) == 11

def test_quick_sort_partitioning_1():
    assert find_Kth_smallest_number_quick_sort_partitioning([1, 5, 12, 2, 11, 5], 3) == 5

def test_quick_sort_partitioning_2():
    assert find_Kth_smallest_number_quick_sort_partitioning([1, 5, 12, 2, 11, 5], 4) == 5

def test_quick_sort_partitioning_3():
    assert find_Kth_smallest_number_quick_sort_partitioning([5, 12, 11, -1, 12], 3) == 11

def test_quick_sort_randomized_partitioning_1():
    assert find_Kth_smallest_number_quick_sort_randomized_partitioning([1, 5, 12, 2, 11, 5], 3) == 5

def test_quick_sort_randomized_partitioning_2():
    assert find_Kth_smallest_number_quick_sort_randomized_partitioning([1, 5, 12, 2, 11, 5], 4) == 5

def test_quick_sort_randomized_partitioning_3():
    assert find_Kth_smallest_number_quick_sort_randomized_partitioning([5, 12, 11, -1, 12], 3) == 11

def test_median_of_medians_1():
    assert find_Kth_smallest_number_median_of_medians([1, 5, 12, 2, 11, 5], 3) == 5

def test_median_of_medians_2():
    assert find_Kth_smallest_number_median_of_medians([1, 5, 12, 2, 11, 5], 4) == 5

def test_median_of_medians_3():
    assert find_Kth_smallest_number_median_of_medians([5, 12, 11, -1, 12], 3) == 11
