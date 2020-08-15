def add_to_list(head, tail, node):
    if not head:
        head = node
        tail = node
    elif head == tail:
        tail = node
        head.next = node
    else:
        tail.next = node
        tail = node

    return head, tail

def combine_lists(l1_head, l1_tail, l2_head, l2_tail):
    new_head = l1_head if l1_head else l2_head
    new_tail = l2_tail if l2_head else l1_tail

    if l1_tail:
        l1_tail.next = l2_head

    return new_head, new_tail

def rearrangeLinkedList(head, k):
    lt_k_head, lt_k_tail = None, None
    eq_k_head, eq_k_tail = None, None
    gt_k_head, gt_k_tail = None, None

    prev, curr = None, head
    while curr:
        if curr.value < k:
            lt_k_head, lt_k_tail = add_to_list(lt_k_head, lt_k_tail, curr)
        elif curr.value > k:
            gt_k_head, gt_k_tail = add_to_list(gt_k_head, gt_k_tail, curr)
        else:
            eq_k_head, eq_k_tail = add_to_list(eq_k_head, eq_k_tail, curr)

        prev = curr
        curr = curr.next
        prev.next = None


    combined_head, combined_tail = combine_lists(lt_k_head, lt_k_tail, eq_k_head, eq_k_tail)
    new_head, _ = combine_lists(combined_head, combined_tail, gt_k_head, gt_k_tail)
    return new_head


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
