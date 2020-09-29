from algo_exp.linked_list_construction.main import Node, DoublyLinkedList


def get_node_values_head_to_tail(linked_list):
    values = []
    node = linked_list.head
    while node is not None:
        values.append(node.value)
        node = node.next
    return values


def get_node_values_tail_to_head(linked_list):
    values = []
    node = linked_list.tail
    while node is not None:
        values.append(node.value)
        node = node.prev
    return values


def bind_nodes(node_one, node_two):
    node_one.next = node_two
    node_two.prev = node_one

def test_1():
    linked_list = DoublyLinkedList()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    three2 = Node(3)
    three3 = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    bind_nodes(one, two)
    bind_nodes(two, three)
    bind_nodes(three, four)
    bind_nodes(four, five)
    linked_list.head = one
    linked_list.tail = five

    linked_list.set_head(four)
    assert get_node_values_head_to_tail(linked_list) == [4, 1, 2, 3, 5]
    assert get_node_values_tail_to_head(linked_list) == [5, 3, 2, 1, 4]

    linked_list.set_tail(six)
    assert get_node_values_head_to_tail(linked_list) == [4, 1, 2, 3, 5, 6]
    assert get_node_values_tail_to_head(linked_list) == [6, 5, 3, 2, 1, 4]

    linked_list.insert_before(six, three)
    assert get_node_values_head_to_tail(linked_list) == [4, 1, 2, 5, 3, 6]
    assert get_node_values_tail_to_head(linked_list) == [6, 3, 5, 2, 1, 4]

    linked_list.insert_after(six, three2)
    assert get_node_values_head_to_tail(linked_list) == [4, 1, 2, 5, 3, 6, 3]
    assert get_node_values_tail_to_head(linked_list) == [3, 6, 3, 5, 2, 1, 4]

    linked_list.insert_at_position(1, three3)
    assert get_node_values_head_to_tail(linked_list) == [3, 4, 1, 2, 5, 3, 6, 3]
    assert get_node_values_tail_to_head(linked_list) == [3, 6, 3, 5, 2, 1, 4, 3]

    linked_list.remove_nodes_with_value(3)
    assert get_node_values_head_to_tail(linked_list) == [4, 1, 2, 5, 6]
    assert get_node_values_tail_to_head(linked_list) == [6, 5, 2, 1, 4]

    linked_list.remove(two)
    assert get_node_values_head_to_tail(linked_list) == [4, 1, 5, 6]
    assert get_node_values_tail_to_head(linked_list) == [6, 5, 1, 4]

    assert linked_list.contains_node_with_value(5) is True


def test_2():
    one = Node(1)
    linked_list = DoublyLinkedList()
    linked_list.insert_at_position(1, one)

    assert get_node_values_head_to_tail(linked_list) == [1]
    assert get_node_values_tail_to_head(linked_list) == [1]
