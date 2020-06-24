def balancedBrackets(string):
    closing = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    bracket = set('{}()[]')

    stack = []

    for char in string:
        if char not in bracket:
            continue
        if char in closing:
            stack.append(closing[char])
        elif not stack or stack.pop() != char:
            return False

    return len(stack) == 0
