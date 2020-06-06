class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opposite = {
            '(': ')',
            '[': ']',
            '{': '}'
        }

        i = 0
        while i < len(s):
            l = s[i]
            if l in opposite:
                stack.append(opposite[l])
            else:
                if not stack or stack.pop() != l:
                    return False
            i += 1

        return len(stack) == 0
