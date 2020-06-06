from unittest import TestCase, main
from main import Solution
from leet.data_structures.list_node import ListNode

s = Solution()


class TestSuite(TestCase):
    def test_1(self):
        list1 = ListNode(1, ListNode(2, ListNode(4)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        expected = ListNode(1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4))))))
        self.assertTrue(ListNode.compare(expected, s.mergeTwoLists(list1, list2)))

    def test_2(self):
        list1 = None
        list2 = ListNode(0)
        expected = ListNode(0)
        self.assertTrue(ListNode.compare(expected, s.mergeTwoLists(list1, list2)))


if __name__ == '__main__':
    main()
