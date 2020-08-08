def shortenPath(path):
    arr = path.split('/')
    stack = []
    if path[0] == '/':
        stack.append('')
    for char in arr:
        if char == '' or char == '.':
            continue

        if char == '..':
            if not stack or stack[-1] == '..':
                stack.append(char)
            elif stack[-1] != '':
                stack.pop()
        else:
            stack.append(char)

    ans = '/'.join(stack)
    return ans if ans else '/'
