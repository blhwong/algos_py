from data_structures.list_node import ListNode

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        arr = []

        if not head:
            return None

        curr = head
        while curr:
            arr.append(curr)
            curr = curr.next

        start, end = 0, len(arr) - 1

        while start < end:
            arr[start].next, arr[end].next = arr[end], arr[start + 1]
            start += 1
            end -= 1

        if len(arr) % 2 == 0:
            arr[start].next = None
        else:
            arr[end].next = None

        return head
