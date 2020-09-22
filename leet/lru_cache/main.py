class ListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev, self.next = None, None

    def remove_bindings(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev, self.next = None, None


class DoublyLinkedList:

    def __init__(self):
        self.head, self.tail = None, None

    def set_head(self, node):
        if self.head == node:
            return
        if not self.head:
            self.head, self.tail = node, node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            node.remove_bindings()
            self.head.prev = node
            node.next = self.head
            self.head = self.head.prev

    def remove_tail(self):
        if not self.tail:
            return
        if self.tail == self.head:
            self.head, self.tail = None, None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.size = capacity
        self.storage = {}
        self.list = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key not in self.storage:
            return -1
        self.list.set_head(self.storage[key])
        return self.storage[key].value

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.storage:
            node = self.storage[key]
            node.value = value
        else:
            node = ListNode(key, value)

        self.storage[key] = node
        self.list.set_head(node)

        if len(self.storage) > self.size:
            tail = self.list.tail
            self.list.remove_tail()
            del self.storage[tail.key]
