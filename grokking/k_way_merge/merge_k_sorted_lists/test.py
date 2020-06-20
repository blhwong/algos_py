from unittest import TestCase, main
from grokking.k_way_merge.merge_k_sorted_lists.main import merge_lists
from data_structures.list_node import ListNode


class TestSuite(TestCase):
    def test_1(self):
        l1 = ListNode(2, ListNode(6, ListNode(8)))
        l2 = ListNode(3, ListNode(6, ListNode(7)))
        l3 = ListNode(1, ListNode(3, ListNode(4)))
        expected = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(4, ListNode(6, ListNode(6, ListNode(7, ListNode(8)))))))))
        self.assertTrue(ListNode.compare(merge_lists([l1, l2, l3]), expected))

    def test_2(self):
        l1 = ListNode(5, ListNode(8, ListNode(9)))
        l2 = ListNode(1, ListNode(7))
        expected = ListNode(1, ListNode(5, ListNode(7, ListNode(8, ListNode(9)))))
        self.assertTrue(ListNode.compare(merge_lists([l1, l2]), expected))

if __name__ == '__main__':
    main()
