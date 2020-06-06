from unittest import TestCase, main
from leet.data_structures.list_node import ListNode

class TestSuite(TestCase):
    def test_compare_false(self):
        list1 = ListNode(1, ListNode(4, ListNode(5)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))

        self.assertFalse(ListNode.compare(list1, list2))

    def test_compare_true(self):
        list1 = ListNode(1, ListNode(2, ListNode(3)))
        list2 = ListNode(1, ListNode(2, ListNode(3)))

        self.assertTrue(ListNode.compare(list1, list2))

    def test_repr(self):
        list1 = ListNode(1, ListNode(2, ListNode(3)))

        expected = '1->2->3'

        self.assertEqual(repr(list1), expected)



if __name__ == '__main__':
    main()
