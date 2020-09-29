from algo_exp.min_max_stack.main import MinMaxStack


def test_1():
    stack = MinMaxStack()

    stack.push(5)
    assert stack.get_min() == 5
    assert stack.get_max() == 5
    assert stack.peek() == 5

    stack.push(7)
    assert stack.get_min() == 5
    assert stack.get_max() == 7
    assert stack.peek() == 7

    stack.push(2)
    assert stack.get_min() == 2
    assert stack.get_max() == 7
    assert stack.peek() == 2

    assert stack.pop() == 2
    assert stack.pop() == 7

    assert stack.get_min() == 5
    assert stack.get_max() == 5
    assert stack.peek() == 5
