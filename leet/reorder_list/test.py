from unittest import TestCase, main
from leet.reorder_list.main import Solution
from data_structures.list_node import ListNode

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        result = s.reorderList(i)
        expected = ListNode(1, ListNode(4, ListNode(2, ListNode(3))))
        self.assertTrue(ListNode.compare(result, expected))

    def test_2(self):
        i = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
        result = s.reorderList(i)
        expected = ListNode(1, ListNode(5, ListNode(2, ListNode(4, ListNode(3)))))
        self.assertTrue(ListNode.compare(result, expected))


if __name__ == '__main__':
    main()
