from algo_exp.interweaving_strings.main import interweavingStrings


def test_1():
    assert interweavingStrings('algoexpert', 'your-dream-job', 'your-algodream-expertjob') is True

def test_2():
    assert interweavingStrings('a', 'b', 'ac') is False

def test_3():
    assert interweavingStrings('algoexpert', 'your-dream-job', 'your-algodream-expertjo') is False
