from data_structures.binary_search_tree.main import BST
from collections import deque

def minHeightBst(array):
    ans = None
    q = deque()
    left, right = 0, len(array) - 1
    q.append((left, right))
    while q:
        left, right = q.popleft()
        if right < left:
            continue
        mid = (left + right) // 2
        if ans:
            ans.insert(array[mid])
        else:
            ans = BST(array[mid])
        q.append((left, mid - 1))
        q.append((mid + 1, right))

    return ans
