class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def remove_bindings(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node):
        if self.head == node:
            return
        if not self.head:
            self.head = node
            self.tail = node
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
            self.head = node


    def remove_tail(self):
        if not self.tail:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None

# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.storage = {}
        self.most_recent_list = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        node = None
        if key in self.storage:
            self.storage[key].value = value
            node = self.storage[key]
        else:
            node = ListNode(key, value)
            self.storage[key] = node
        self.most_recent_list.set_head(node)

        if len(self.storage) > self.maxSize:
            node_to_evict = self.most_recent_list.tail
            self.most_recent_list.remove_tail()
            del self.storage[node_to_evict.key]


    def getValueFromKey(self, key):
        if key not in self.storage:
            return None
        v = self.storage[key].value
        self.most_recent_list.set_head(self.storage[key])
        return v

    def getMostRecentKey(self):
        return self.most_recent_list.head.key
