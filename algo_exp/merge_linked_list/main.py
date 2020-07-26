def mergeLinkedLists(headOne, headTwo):
    head, tail = None, None
    while headOne or headTwo:
        curr = None
        if headOne and not headTwo:
            tail.next = headOne
            break
        if not headOne and headTwo:
            tail.next = headTwo
            break

        if headOne.value < headTwo.value:
            curr = headOne
            headOne = headOne.next
        else:
            curr = headTwo
            headTwo = headTwo.next

        if not head:
            head = curr
            tail = curr
        else:
            tail.next = curr
            tail = tail.next

    return head
