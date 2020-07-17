def calculate(input_string):
    ans = 0
    operand = 0
    sign = 1
    stack = []

    for char in input_string:
        if char.isdigit():
            operand = operand * 10 + int(char)
        elif char == '+':
            ans += sign * operand
            sign = 1
            operand = 0
        elif char == '-':
            ans += sign * operand
            sign = -1
            operand = 0
        elif char == '(':
            stack.append(ans)
            stack.append(sign)
            sign = 1
            ans = 0
        elif char == ')':
            ans += sign * operand
            ans *= stack.pop()
            ans += stack.pop()
            operand = 0

    return ans + sign * operand
