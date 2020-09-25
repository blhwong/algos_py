import math


class Solution:

    def calculate(self, s: str) -> int:
        if not s:
            return 0

        stack = []
        num, operation = 0, '+'

        for char in s + '+':
            if char.isdigit():
                num = num * 10 + int(char)
            elif char != ' ':
                if operation == '+':
                    stack.append(num)
                elif operation == '-':
                    stack.append(-num)
                elif operation == '*':
                    stack.append(stack.pop() * num)
                elif operation == '/':
                    stack.append(math.trunc(stack.pop() / num))

                operation = char
                num = 0

        return sum(stack)
