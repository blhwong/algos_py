class Node:

    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        pass

    def set_tail(self, node):
        pass

    def insert_before(self, node, node_to_insert):
        pass

    def insert_after(self, node, node_to_insert):
        pass

    def insert_at_position(self, position, node_to_insert):
        pass

    def remove_nodes_with_value(self, value):
        pass

    def remove(self, node):
        pass

    def contains_node_with_value(self, value):
        pass
