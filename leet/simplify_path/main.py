class Solution:

    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')
        stack = ['']

        for char in arr:
            if char in ['', '.']:
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
