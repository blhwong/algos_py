def find_cycle_start(head):
    def get_cycle_length(slow):
        curr = slow
        ans = 0
        while True:
            curr = curr.next
            ans += 1
            if curr == slow:
                break
        return ans

    def get_cycle(head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

    def move(head, cycle_length):
        pointer = head
        count = cycle_length
        while count > 0:
            pointer = pointer.next
            count -= 1
        return pointer


    cycle = get_cycle(head)
    cycle_length = get_cycle_length(cycle)


    p1 = head
    p2 = move(head, cycle_length)

    if p1 == p2:
        return p1

    while True:
        p1 = p1.next
        p2 = p2.next
        if p1 == p2:
            return p1

