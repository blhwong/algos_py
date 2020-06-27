from typing import List
from data_structures.list_node import ListNode
from heapq import *

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        min_heap = []
        for i in range(len(lists)):
            curr_list = lists[i]
            if curr_list:
                heappush(min_heap, (curr_list.val, i, curr_list))

        head, tail = None, None

        while min_heap:
            val, i, curr_list = heappop(min_heap)
            if curr_list.next:
                heappush(min_heap, (curr_list.next.val, i, curr_list.next))

            if not head:
                head = ListNode(val)
                tail = head
            else:
                if not head.next:
                    head.next = tail
                tail.next = ListNode(val)
                tail = tail.next

        return head
