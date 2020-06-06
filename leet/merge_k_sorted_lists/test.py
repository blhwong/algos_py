from unittest import TestCase, main
from main import Solution
from leet.data_structures.list_node import ListNode

s = Solution()

class TestSuite(TestCase):
    def test_1(self):
        list1 = ListNode(1, ListNode(4, ListNode(5)))
        list2 = ListNode(1, ListNode(3, ListNode(4)))
        list3 = ListNode(2, ListNode(6))
        lists = [
            list1,
            list2,
            list3
        ]
        expected = (
            ListNode(1, ListNode(1, ListNode(
                2, ListNode(3, ListNode(
                    4, ListNode(4, ListNode(
                        5, ListNode(6))))))))
        )
        self.assertTrue(ListNode.compare(
            expected, s.mergeKLists(lists)))

if __name__ == '__main__':
    main()
