from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        count = 0
        cycles = len(self.q)
        self.q.appendleft(x)
        while count < cycles:
            self.q.appendleft(self.q.pop())
            count += 1

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0

